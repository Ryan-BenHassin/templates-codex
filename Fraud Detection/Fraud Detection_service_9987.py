import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class FraudDetection:
 def __init__(self, data):
 self.data = data

 def preprocess(self):
 X = self.data.drop('fraudulent', axis=1)
 y = self.data['fraudulent']
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 return X_train, X_test, y_train, y_test

 def train(self, X_train, y_train):
 clf = RandomForestClassifier(n_estimators=100, random_state=42)
 clf.fit(X_train, y_train)
 return clf

 def evaluate(self, clf, X_test, y_test):
 y_pred = clf.predict(X_test)
 print("Accuracy:", accuracy_score(y_test, y_pred))
 print("Classification Report:\n", classification_report(y_test, y_pred))
 print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

 def predict(self, clf, data):
 return clf.predict(data)

# Load data
data = pd.read_csv('fraud_data.csv')

# Initialize fraud detection model
fd = FraudDetection(data)

# Preprocess data
X_train, X_test, y_train, y_test = fd.preprocess()

# Train model
clf = fd.train(X_train, y_train)

# Evaluate model
fd.evaluate(clf, X_test, y_test)

# Make predictions
new_data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
predictions = fd.predict(clf, new_data)
print("Predictions:", predictions)
