import re
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class DataValidator:
    def __init__(self, data):
        self.data = data

    def validate_phone_number(self, column_name):
        pattern = re.compile('^[0-9]{10,12}$')
        result = []
        for phone in self.data[column_name]:
            if pattern.match(str(phone)):
                result.append(True)
            else:
                result.append(False)
        return result

    def validate_email(self, column_name):
        pattern = re.compile(r'[^@]+@[^@]+\.[^@]+')
        result = []
        for email in self.data[column_name]:
            if pattern.match(str(email)):
                result.append(True)
            else:
                result.append(False)
        return result

    def validate_credit_card(self, column_name):
        pattern = re.compile(r'^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9]{12}|4[4-9][0-9]{12}|2[2-9][0-9]{12}|1(?:[2-8][0-9]{12}|9[0-9]{11,12}))|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9][0-9]{12}|4[4-9][0-9]{12}|2[2-9][0-9]{12}|1(?:[2-8][0-9]{12}|9[0-9]{11,12}))$')
        result = []
        for card in self.data[column_name]:
            if pattern.match(str(card)):
                result.append(True)
            else:
                result.append(False)
        return result

    def validate_zipcode(self, column_name):
        pattern = re.compile('^[0-9]{5}(?:-[0-9]{4})?$')
        result = []
        for zipcode in self.data[column_name]:
            if pattern.match(str(zipcode)):
                result.append(True)
            else:
                result.append(False)
        return result

    def outlier_detection(self, column_name):
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(self.data[[column_name]])
        result = []
        for value in scaled_data:
            if value > 1 or value < 0:
                result.append(True)
            else:
                result.append(False)
        return result

data = pd.read_csv('data.csv')
validator = DataValidator(data)
print(validator.validate_phone_number('phone'))
print(validator.validate_email('email'))
print(validator.validate_credit_card('credit_card'))
print(validator.validate_zipcode('zipcode'))
print(validator.outlier_detection('values'))