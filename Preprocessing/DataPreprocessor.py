import os
import yaml
from tqdm import tqdm
from torch.utils.data import IterableDataset, DataLoader
from Preprocessing.DataReaders.JSONParser import JSONParser
from Preprocessing.Exceptions.ConfigNotFound import ConfigNotFound
from Preprocessing.Exceptions.InvalidInputDataType import InvalidInputDataType
from Preprocessing.Exceptions.FieldErrors import TextFieldNotFound, LabelFieldNotFound

#               TODO's
# 20 TODO add a make config template function
# 30 TODO is_config_valid. Add once all transforms are defined
# 37 TODO list transformations and order them according to whether they listed and are active
# 94 TODO Check if text field is None: log as missing give iteration number so can find later
# 95 TODO Check if text field is a non-empty str: Log if not with iteration number
# 96 TODO Check if label field is None: log as missing give iteration number so can find later
# 97 TODO Check if label field is a non-empty int or float: Log if not with iteration number
#    TODO In Logs calculate the average and min and max sentiment rating, count and map labels to data points so
#    that they can be normalised and balanced


class DataPreprocessor(IterableDataset):

    def __init__(self):

        self.parser = None

        try:
            if not self.is_config_available():
                raise ConfigNotFound()

            self.config = self.read_config()


            self.identify_parser()

            if self.config['save_config']:
                self.save_config()




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


    def preprocess_text(self, text_data):

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





if __name__ == "__main__":
    dataset = DataPreprocessor()
    dataLoader = DataLoader(dataset, batch_size=64)

    for batch in dataLoader:
        print(batch)