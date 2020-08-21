# text_field = self.config['fields']['text']['name']
# label_field = self.config['fields']['label']['name']
#
# if text_field not in data.keys():
#     raise TextFieldNotFound(expectedField=text_field)
#
# if label_field not in data.keys():
#     raise LabelFieldNotFound(expectedField=label_field)
#
# text_data = data[text_field]
# label_data = data[label_field]
#
# # TODO Check if text field is None: log as missing give iteration number so can find later
# # TODO Check if text field is a non-empty str: Log if not with iteration number
# # TODO Check if label field is None: log as missing give iteration number so can find later
# # TODO Check if label field is a non-empty int or float: Log if not with iteration number