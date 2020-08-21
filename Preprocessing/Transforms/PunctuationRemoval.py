
class PunctuationRemoval:

    def __init__(self, omissions):

        #TODO if bert tokenizer is used then class should omit BERT special chars like ## check huggingface docs

        self.special_chars = {'!': True, '@': True, '£': True, '€': True, '#':True, '$':True, '%':True,
                         '^':True, '&':True, '*':True, '(':True, ')':True, "_":True, "-":True, "+":True,
                         "=":True, "{":True, "[":True, "}":True, "]":True, ":":True, ";":True, '"':True,
                         "'":True, "|":True, "r'\'":True, "<":True, ">":True, ",":True, ".":True, "?":True,
                         "/":True, "§":True, "±":True}

        self.omissions = self.init_omissions(omissions)


    def init_omissions(self, omissions):
        output_dic = {}
        for o in omissions:
            try:
                val = output_dic[o]

            except KeyError as e:
                output_dic[o] = True

        return output_dic


    def is_special_char(self, token):

        # if it has not been listed as character  ignore then proceed
        if not self.omissions[token]:
            try:
                self.special_chars[token]
                return True
            except:
                return False


if __name__ == '__main__':
    sentence1 = "Hello! my name is gary$ { | and i like <html>"