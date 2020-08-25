

class Transform:

    def __init__(self, config):
        self.config = config

    def __call__(self, text_data):
        return ' '.join(text_data)