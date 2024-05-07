#TODO
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

class FraudDetectionService:
 def __init__(self, model_path='fraudDetectionModel.pkl'):
 self.model = self.load_model(model_path)

 def load_model(self, model_path):
 try:
 with open(model_path, 'rb') as f:
 return pickle.load(f)
 except FileNotFoundError:
 return self.train_model()

 def train_model(self):
 data = pd.read_csv('fraud_data.csv')
 X = data.drop(['isFraud'], axis=1)
 y = data['isFraud']

 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

 model = RandomForestClassifier(n_estimators=100, random_state=42)
 model.fit(X_train, y_train)

 y_pred = model.predict(X_test)
 print('Model Accuracy:', accuracy_score(y_test, y_pred))
 print('Classification Report:\n', classification_report(y_test, y_pred))
 print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))

 with open('fraudDetectionModel.pkl', 'wb') as f:
 pickle.dump(model, f)

 return model

 def detect_fraud(self, transaction_data):
 return self.model.predict(transaction_data)

# Example usage
service = FraudDetectionService()
transaction_data = pd.DataFrame([{'amount': 100, 'category': 'A', 'country': 'US'}])
result = service.detect_fraud(transaction_data)
print('Fraud Detection Result:', result)
