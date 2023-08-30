class MyString:
    def __init__(self, value=""):
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not self.value:
            return 0
        sentences = [s.strip() for s in self.value.split('.') if s.strip()]
        return len(sentences)


if __name__ == "__main__":
    string = MyString("Hello, world!")
    print(string.is_sentence())  # False
    print(string.is_question())  # False
    print(string.is_exclamation())  # True
    print(string.count_sentences())  # 1
