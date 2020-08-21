
class InvalidInputDataType (Exception):

    def __init__(self):

        self.message = "DataPreprocessor could not find a valid input data type. Currently supported types are" \
                       "json"

    def __str__(self):
        return f"InvalidInputDataType: {self.message}"