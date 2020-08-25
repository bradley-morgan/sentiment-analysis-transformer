from nltk.stem import WordNetLemmatizer

class Transform:

    def __init__(self, config):
        self.config = config
        self.lemmatizer = WordNetLemmatizer()

        a = self.lemmatizer.lemmatize('childrens')

        if self.config['cache']:
            self.cache = {}
            # speed up lemmatizer cache results so if the same word comes up again just query the dict rather running
            # lemmatizer again as dict lookup is o(1) complexity


    def __call__(self, token_sequence):

        output_token_sequence = []
        cache_use = 0
        for token in token_sequence:
            try:
                cached_lemma = self.cache[token]
                output_token_sequence.append(cached_lemma)
                cache_use += 1

            except KeyError as e:
                d = e.args[0]
                lemma = self.lemmatizer.lemmatize(token)
                output_token_sequence.append(lemma)
                if self.config['cache']:
                    self.cache[token] = lemma

        if self.config['cache']  and self.config['cache_per_sample']:
            self.cache = {}

        return output_token_sequence

