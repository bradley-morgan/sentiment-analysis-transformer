from nltk.corpus import stopwords

class Transform:

    def __init__(self, config):

        self.config = config
        self.stop_words = {}
        for word in stopwords.words('english'):
            self.stop_words[word] = True


    def __call__(self, token_sequence):

        output_token_sequence = []
        for token in token_sequence:
            try:
                _ = self.stop_words[token]
            except KeyError as e:
                output_token_sequence.append(token)

        return output_token_sequence
