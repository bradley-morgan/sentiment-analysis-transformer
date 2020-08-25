
class TextFieldNotFound (Exception) :
    def __init__(self, expectedField=None, custom_message=None):

        if custom_message == None:
            self.message = f"DataPreprocessor could not find the field {expectedField} in data set. Please check dataset structure"
        else:
            self.message = custom_message

    def __str__(self):
        return f"TextFieldNotFound: {self.message}"


class LabelFieldNotFound (Exception):
    def __init__(self, expectedField=None, custom_message=None):

        if custom_message == None:
            self.message = f"DataPreprocessor could not find the field {expectedField} in data set. Please check dataset structure"
        else:
            self.message = custom_message

    def __str__(self):
        return f"LabelFieldNotFound: {self.message}"