
class Transform:

    def __init__(self, config):
        self.state = True
        self.config = config

    def __call__(self, input_data):
        return [input_data, "TEST TRANSFORM"]