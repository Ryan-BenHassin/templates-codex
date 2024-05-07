import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def machine_learning_service(X, y):
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

 regressor = LinearRegression() 
 regressor.fit(X_train, y_train)

 y_pred = regressor.predict(X_test)

 print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred)) 
 print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred)) 
 print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

 return y_pred

api_key = 'YOUR_API_KEY_HERE'
url = 'https://example.com/get_data'
data = requests.get(url, headers={'Authorization': api_key}).json()

X = pd.DataFrame(data['X'])
y = pd.DataFrame(data['y'])

machine_learning_service(X, y)
