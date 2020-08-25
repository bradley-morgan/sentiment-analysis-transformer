class LowerInvalidInput (Exception):

    def __init__(self, custom_message=None):

        if custom_message == None:
            self.message = "Lower.py transform function received an invalid input type, data must be either a list or " \
                           "a string type"
        else:
            self.message = custom_message

    def __str__(self):
        return f"LowerInvalidInput: {self.message}"