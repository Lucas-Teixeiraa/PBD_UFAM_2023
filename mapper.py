import sys
import io
import re
import nltk
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
stop_words = set(stopwords.words('english'))
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')

class Mapper:

  def __init__(self):
    self.array= dict()

  def Map(self):
    for line in input_stream:
      line = line.strip()
      line = re.sub(r'[^\w\s]', '',line)
      line = line.lower()

      for x in line:
        if x in punctuations:
          line=line.replace(x, " ") 

      words=line.split()
      for word in words: 
        if word not in stop_words:
          if word in self.array.keys():
              self.array[word] = self.array[word] + 1
          else:
              self.array[word] = 1

  def Close(self):
    for term in self.array.keys():
          print("%s\t%s" % (term, self.array[term]))


if __name__ == "__main__":
    mapeador = Mapper()
    mapeador.Map()
    mapeador.Close()
