import gzip
import json
import os
import yaml
from Preprocessing.Exceptions.ConfigNotFound import ConfigNotFound as ConfigNotFound


class DataPreprocessor:

    def __init__(self):

        # check if config exists
        # read config
        # Check all parameters are there
        # save config if true
        # init main processing loop

        try:
            if not self.is_config_available():
                raise ConfigNotFound()
                #TODO add a make config template function

            self.config = self.read_config()

            # TODO is_config_valid. Add once all transforms are defined

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






if __name__ == "__main__":
    DataPreprocessor()