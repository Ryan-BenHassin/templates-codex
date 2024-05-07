import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd

# Load the dataset
df = pd.read_csv("your_data.csv")

# Preprocess the data
X = df[['feature1', 'feature2', ...]] # feature columns
y = df['target'] # target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression object and train the model
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = logreg.predict(X_test)

# Evaluate the model using accuracy score
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
