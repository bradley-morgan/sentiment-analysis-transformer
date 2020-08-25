
class Transform:

    def __init__(self, config):

        self.config = config

        self.special_chars = {'!': True, '@': True, '£': True, '€': True, '#':True, '$':True, '%':True,
                         '^':True, '&':True, '*':True, '(':True, ')':True, "_":True, "-":True, "+":True,
                         "=":True, "{":True, "[":True, "}":True, "]":True, ":":True, ";":True, '"':True,
                         "'":True, "|":True, "'\'":True, "<":True, ">":True, ",":True, ".":True, "?":True,
                         "/":True, "§":True, "±":True}

        self.omissions = self.init_omissions(config['omissions'])
        self.inRecursive_state = False

    def init_omissions(self, omissions):
        output_dic = {}
        omissions = omissions.strip()
        if not omissions:
            return output_dic

        for o in omissions:
            try:
                _ = output_dic[o]

            except KeyError as e:
                output_dic[o.strip()] = True

        return output_dic


    def __call__(self, token_sequence):

        output_token_sequence = []
        for token in token_sequence:

            try:
                _ = self.omissions[token]
                output_token_sequence.append(token)

            except KeyError as e:

                try:
                    _ = self.special_chars[token]

                except KeyError as e:
                    if self.config['within_word'] and not self.inRecursive_state:
                        self.inRecursive_state = True
                        token = self(list(token))
                        self.inRecursive_state = False
                    output_token_sequence.append(token)

        if self.inRecursive_state:
            return ''.join(output_token_sequence)

        return output_token_sequence

