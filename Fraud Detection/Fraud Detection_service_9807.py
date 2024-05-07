import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class FraudDetection:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X, y):
        y_pred = self.model.predict(X)
        print("Accuracy:", accuracy_score(y, y_pred))
        print("Classification Report:\n", classification_report(y, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y, y_pred))

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # preprocess the data as per requirement
    # for example
    df['amount'] = df['amount'].astype(float)
    return df

def main():
    file_path = 'fraud_data.csv'  # replace with your file path
    df = load_data(file_path)
    df = preprocess_data(df)

    X = df.drop('is_fraud', axis=1)
    y = df['is_fraud']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    fd = FraudDetection()
    fd.train(X_train, y_train)
    fd.evaluate(X_test, y_test)

if __name__ == "__main__":
    main()