class Word(str):
    def __init__(self, word: str):
        self.text = word

    def __repr__(self) -> str:
        return f"Word(text={self.text}, freq={self.freq})"
    
    def __str__(self) -> str:
        return self.text


class WordGroup:
    def __init__(self, word_tuple, freq):
        self.word_tuple = word_tuple
        self.text = ''.join(word.text for word in word_tuple)
        self.freq = freq

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.freq == other.freq

    def __lt__(self, other) -> bool:
        if self.freq < other.freq:
            return True
        elif self.freq == other.freq:
            if len(self.word_tuple[0].text) < len(other.word_tuple[0].text):
                return True
            elif len(self.word_tuple[0].text) == len(other.word_tuple[0].text):
                return self.text < other.text
            else:
                return False
        else:
            return False
        
    def __gt__(self, other) -> bool:
        return not self.__eq__(other) and not self.__lt__(other)
        
    def to_Word(self):
        return Word(self.text)


class Text:
    def __init__(self, word_list=None, row_freq=None):
        if word_list is None:
            self.word_list = []
            self.row_freq = []
        else:
            self.word_list = word_list
            self.row_freq = row_freq
        self.row_length = [len(i) for i in self.word_list]

    def append_row(self, word_list, freq):
        self.word_list.append(word_list)
        self.row_freq.append(freq)

    def count(self):
        ...

    def group(self):
        ...

    def is_all_done(self):
        return all(length == 1 for length in self.row_length)


n, m = map(int, input().split())

raw_text_list = []
for _ in range(n):
    input_ = input().split()
    raw_text_list.append(input_[0], int(input_[1]))

txt = Text()
for s, f in raw_text_list:
    word_list = [Word(i) for i in s]
    txt.append_row(word_list, f)

word_dict = []
chars = list(set(''.join([item[0] for item in raw_text_list]).split()))
chars.sort()
for c in chars:
    word_dict.append(Word(c))

