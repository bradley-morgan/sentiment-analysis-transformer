
class TextFieldNotFound (Exception) :
    def __init__(self, expectedField):

        self.message = f"DataPreprocessor could not find the field {expectedField} in data set. Please check dataset structure"

    def __str__(self):
        return f"TextFieldNotFound: {self.message}"


class LabelFieldNotFound (Exception):
    def __init__(self, expectedField):

        self.message = f"DataPreprocessor could not find the field {expectedField} in data set. Please check dataset structure"

    def __str__(self):
        return f"LabelFieldNotFound: {self.message}"