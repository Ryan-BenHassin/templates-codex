import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Place holder for api_key
api_key = "your_api_key_here"

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def process_text(text):
 tokens = word_tokenize(text.lower())
 tokens = [t for t in tokens if t.isalpha()]
 stop_words = set(stopwords.words('english'))
 tokens = [t for t in tokens if t not in stop_words]
 lemmatizer = WordNetLemmatizer()
 tokens = [lemmatizer.lemmatize(t) for t in tokens]
 return '.join(tokens)

def train(text_data, labels):
 vectorizer = CountVectorizer()
 X = vectorizer.fit_transform(text_data)
 y = labels
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 clf = MultinomialNB()
 clf.fit(X_train, y_train)
 y_pred = clf.predict(X_test)
 print("Accuracy: ", accuracy_score(y_test, y_pred))
 print("Classification Report:\n", classification_report(y_test, y_pred))
 print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
 return clf, vectorizer

def predict(text, clf, vectorizer):
 text = process_text(text)
 text = [text]
 X = vectorizer.transform(text)
 pred = clf.predict(X)
 return pred[0]

# Example usage
text_data = ["This is a sample text.", "I love machine learning.", "Natural Language Processing is fun."]
labels = [0, 1, 1]
clf, vectorizer = train(text_data, labels)
print(predict("This is another sample text.", clf, vectorizer))
