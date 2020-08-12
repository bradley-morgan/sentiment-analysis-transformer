
class ConfigNotFound (Exception):

    def __init__(self):

        self.message = "DataPreprocessor could not find a valid config.yaml file please create one using MakeConfigFile()" \
                       "place a valid config file into the same directory as DataPreprocessor.py"

    def __str__(self):
        return f"ConfigNotFound: {self.message}"