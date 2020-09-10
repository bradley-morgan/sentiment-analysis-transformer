import torch
from transformers import BertModel, AutoTokenizer, BertConfig


# TODO dims = [batch_size, token_seq_length, hidden_states)]
# TODO need [:, 0, :] need all sentence in batch and CLS token encoded at poition 0 at the start of the sentence
# represents as an output the embedding vector for the entire sentence. the rest encode embeddings for each
#individual word.
# TODO Need option to either extract just last layer outputs, average, concat or sum last 4 layers
# TODO Need to formulate this into a class and figure out how the config should work relative to GLOVE
# Just make it so Bert has a config shape and Glove does (glove is max vocab )

PRE_TRAINED_MODEL_NAME = 'bert-base-cased'
tokensizer = AutoTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)


example_text = ['When was I last outside? I am stuck at home for 2 weeks.',
                'BERT understands tokens that were in the training set. Everything else can be encoded',
                'marker for ending of a sentence']

# tokens = tokensizer(example_text)
# token_ids = tokensizer.convert_tokens_to_ids(tokens)
#
# print(tokens)
# print(token_ids)

encoding = tokensizer(example_text, padding=True, truncation=True, return_tensors='pt')

BERT_config = BertConfig()
BERT_config.output_hidden_states = True

BERT_Model = BertModel(BERT_config)

last_layer_outputs, _, hidden_states = BERT_Model(input_ids=encoding['input_ids'], attention_mask=encoding['attention_mask'])


a = 0