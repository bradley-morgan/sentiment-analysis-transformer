import re

class Transform:

    def __init__(self, config):
        self.config = config
        self.tokenizer = r"[\w']+|[.,!?;]"

    def __call__(self, input_data):
        return re.findall(self.tokenizer, input_data)