#TODO
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class NaturalLanguageProcessing:
 def __init__(self, text):
 self.text = text
 self.porter = PorterStemmer()

 def tokenize(self):
 return word_tokenize(self.text)

 def remove_stop_words(self):
 tokens = self.tokenize()
 stop_words = set(stopwords.words('english'))
 return [word for word in tokens if word.lower() not in stop_words]

 def stem_words(self):
 tokens = self.remove_stop_words()
 return [self.porter.stem(word) for word in tokens]

# example usage
nlp = NaturalLanguageProcessing("Your text here")
print(nlp.stem_words())
