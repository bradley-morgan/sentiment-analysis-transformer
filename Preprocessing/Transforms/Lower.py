from Preprocessing.Exceptions.Transforms.LowerInvalidInput import LowerInvalidInput


class Transform:

    def __init__(self, config):
        self.config = config

    def __call__(self, input_data):

        if type(input_data) == list:
            return [word.lower() for word in input_data]
        elif type(input_data) == str:
            return input_data.lower()
        else:
            raise LowerInvalidInput()

