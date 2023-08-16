import sys
import io
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict
import string

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class Mapper:

    def __init__(self):
        self.word_counts = defaultdict(int)
        self.punctuations = set(string.punctuation)
        self.stop_words = set(stopwords.words('english'))

    def Map(self):
        input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
        for line in input_stream:
            line = line.strip().lower()
            line = re.sub(r'[^\w\s]', '', line)

            for x in line:
                if x in self.punctuations:
                    line = line.replace(x, " ")

            words = word_tokenize(line)
            for word in words:
                if word not in self.stop_words:
                    self.word_counts[word] += 1

    def Close(self):
        for term, count in self.word_counts.items():
            print("%s\t%s" % (term, count))


if __name__ == "__main__":
    mapeador = Mapper()
    mapeador.Map()
    mapeador.Close()
