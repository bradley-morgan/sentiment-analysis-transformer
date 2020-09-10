import os
import yaml
from collections import OrderedDict
import importlib
from torch.utils.data import IterableDataset, DataLoader
from torch.utils.data.dataloader import default_collate
from Preprocessing.DataReaders.JSONParser import JSONParser
from Preprocessing.Exceptions.ConfigNotFound import ConfigNotFound
from Preprocessing.Exceptions.InvalidInputDataType import InvalidInputDataType
from Preprocessing.Exceptions.FieldErrors import TextFieldNotFound, LabelFieldNotFound

#               TODO's
# 20 TODO add a make config template function
# 30 TODO is_config_valid. Add once all transforms are define
#    TODO Lower case all config inputs
#    TODO make sure listed transforms actaully exist in the transform folder if active if not throw error
# 37 TODO list transformations and order them according to whether they listed and are active
# 94 TODO Check if text field is None: log as missing give iteration number so can find later
# 95 TODO Check if text field is a non-empty str: Log if not with iteration number
# 96 TODO Check if label field is None: log as missing give iteration number so can find later
# 97 TODO Check if label field is a non-empty int or float: Log if not with iteration number
#    TODO In Logs calculate the average and min and max sentiment rating, count and map labels to data points so
#    that they can be normalised and balanced


#               Sub-TODO
#   TODO create all transforms then add check for embeddings after

class DataPreprocessor(IterableDataset):

    def __init__(self):

        self.parser = None
        self.transform_plugins = None
        # Last items get added to transform_list first
        self.essential_plugins = {'BasicTokenizer': {'active': 'essential'}}

        try:
            if not self.is_config_available():
                raise ConfigNotFound()

            self.config = self.read_config()

            if self.config['save_config']:
                self.save_config()

            self.identify_parser()
            self.transforms = self.prepare_transforms()

        except Exception as e:
            raise e

    def is_config_available(self):
       return os.path.isfile('./config.yaml')

    def read_config(self):
        with open(r'./config.yaml') as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)
            return config

    def save_config(self):
        save_path = './Saved_Configurations'
        if not os.path.isdir(save_path):
            os.mkdir(save_path)

        with open(os.path.join(save_path, self.config['config_name']+'.yaml'), 'w') as outfile:
            yaml.dump(self.config, outfile, default_flow_style=False)
            name = self.config['config_name']
            print(f'Configuration file {name} successfully saved to'
                  f' ./Saved_Configurations directory')

    def identify_parser(self):

        if self.config['input_data_type'] == 'json':
            self.parser = JSONParser(self.config['data_source'], self.config['batch_size'])
        else:
            raise InvalidInputDataType()

    def init_transform_plugins(self):
        plugin_files = os.listdir('./Transforms')
        plugins = {}
        for plugin in plugin_files:
            plugins[plugin.lower()] = True

        # TODO Check that all essential plugins exist in the transforms folder

        self.transform_plugins = plugins

    def prepare_essential_plugins(self, transform_config):
        # Add any transforms that must always be performed here e.g tokenizer
        if len(transform_config) > 0:
            #  if there any optional plugins then they need applying before BERT based tokenzation
            #  BERT tokenizer splits text into word pieces which makes properessing after difficult
            #  thus we need to pretokenization to allow for preprocessing
            for essential_plugin_key, essential_plugin_value in self.essential_plugins.items():
                transform_config[essential_plugin_key] = essential_plugin_value
                transform_config.move_to_end(essential_plugin_key, last=False)

            # Add rejoining of text list to string for BERT retokenization using Word piece
            if self.config['word_embeddings'] == "bert":
                transform_config['RejoinText'] = {'active': 'essential'}

        return transform_config

    def prepare_transforms(self):

        self.init_transform_plugins()
        transform_list = []
        transform_config = self.config['transforms']
        transform_config = OrderedDict(filter(lambda transform: transform[1]['active'] == True, transform_config.items()))

        # Add any transforms that must always be performed here e.g tokenizer
        transform_config = self.prepare_essential_plugins(transform_config)

        for key, plugin_config in transform_config.items():
            try:
                if plugin_config['active'] != 'essential':
                    _ = self.transform_plugins[f'{key.lower()}.py']
                plugin = importlib.import_module(f'Transforms.{key}', package='./Transforms')
                plugin = plugin.Transform(plugin_config)
                transform_list.append(plugin)
            except KeyError as e:
                pass

        return transform_list

    def preprocess_text(self, text_data):

        for transform in self.transforms:
            text_data = transform(text_data)

        return text_data

    def get_stream(self, data):
        # parse dictionary and extract required data field relative to config

        text_field = self.config['fields']['text']['name']
        label_field = self.config['fields']['label']['name']

        if text_field not in data.keys():
            raise TextFieldNotFound(expectedField=text_field)

        if label_field not in data.keys():
            raise LabelFieldNotFound(expectedField=label_field)

        text_data = data[text_field]
        label_data = data[label_field]

        text_data = self.preprocess_text(text_data)

        return text_data, label_data

    def __iter__(self):
        return map(self.get_stream, self.parser)

    def collate_func(self, batch):
        # Kinda weird but it stop pytorch complaining about variable sized batches which i dont care about
        return batch

if __name__ == "__main__":

    dataset = DataPreprocessor()
    dataLoader = DataLoader(dataset, batch_size=64, collate_fn=dataset.collate_func)

    for batch in dataLoader:
        # Creating embeddings using batches rather than line by line more effecient to run the Networks on batches
        print(batch)