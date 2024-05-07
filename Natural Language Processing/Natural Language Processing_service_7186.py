import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('vader_lexicon')

class NLP:
 def __init__(self):
 self.sia = SentimentIntensityAnalyzer()
 self.stop_words = set(stopwords.words('english'))
 self.lemmatizer = WordNetLemmatizer()

 def tokenize(self, text):
 tokens = word_tokenize(text.lower())
 tokens = [word for word in tokens if word not in self.stop_words]
 tokens = [word for word in tokens if word not in string.punctuation]
 tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
 return tokens

 def sentiment_analysis(self, text):
 sentiment_scores = self.sia.polarity_scores(text)
 compound = sentiment_scores['compound']
 if compound > 0.05:
 return 'Positive'
 elif compound < -0.05:
 return 'Negative'
 else:
 return 'Neutral'

 def text_analysis(self, text):
 tokens = self.tokenize(text)
 sentiment = self.sentiment_analysis(text)
 return tokens, sentiment

nlp = NLP()
text = input("Enter a text: ")
tokens, sentiment = nlp.text_analysis(text)
print("Tokens:", tokens)
print("Sentiment:", sentiment)
