import json
import jsonschema
import re
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import requests
import logging
import os
from unittest.mock import patch
import unittest

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Data validation setup
def validate_data(data, schema):
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        logging.error(f"Validation error: {err}")
        return False

# Data validation class
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
        pattern = re.compile(r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12}|3(?:0[0-5]|[68][0-9])[0-9]{11})$')
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
        for value in scaled_data.flatten():
            if value > 1 or value < 0:
                result.append(False)
            else:
                result.append(True)
        return result

# API interaction class
class DataService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.data.gov"

    def headers(self):
        return {"Authorization": f"Bearer {self.api_key}"}

    def get_datasets(self):
        if not self.api_key:
            logging.error("API key is required")
            return {"error": "API key is required", "status_code": 401}
        url = f"{self.base_url}/datasets"
        try:
            response = requests.get(url, headers=self.headers())
            response.raise_for_status()  # This will raise an HTTPError if the response was an error
            return response.json()
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP Error: {e.response.status_code} - {e}")
            return {"error": "HTTP error occurred", "status_code": e.response.status_code, "details": str(e)}
        except json.JSONDecodeError:
            logging.error("Invalid JSON response")
            return {"error": "Invalid JSON response", "status_code": 500}
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return {"error": "An error occurred", "status_code": 500}


def main():
    # Example of initial JSON schema validation
    test_data = {"name": "John", "age": 30}
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "required": ["name", "age"]
    }
    if validate_data(test_data, schema):
        logging.info("Data is valid")
    else:
        logging.error("Data is not valid")

    # Creating a DataFrame with example data for validation
    data = {
        'phone': ['1234567890', '12345678901', '12345', '09876543211', '123456789012'],
        'email': ['test@example.com', 'wrongemail.com', 'user@domain.co.uk', 'another@test.', 'valid.email@address.org'],
        'credit_card': ['4111111111111111', '5500000000000004', '340000000000009', '30000000000004', '6011111111111117'],
        'zipcode': ['12345', '54321-1234', '1234', '98765', '12345-6789'],
        'values': [10, 200, 0, 50, 300]  # This will be used for outlier detection
    }
    df = pd.DataFrame(data)
    validator = DataValidator(df)

    logging.info(f"Phone number validation: {validator.validate_phone_number('phone')}")
    logging.info(f"Email validation: {validator.validate_email('email')}")
    logging.info(f"Credit card validation: {validator.validate_credit_card('credit_card')}")
    logging.info(f"Zipcode validation: {validator.validate_zipcode('zipcode')}")
    logging.info(f"Outlier detection: {validator.outlier_detection('values')}")

    # API Service example usage
    api_key = os.getenv('API_KEY', 'YOUR_API_KEY_HERE')  # Fallback to 'YOUR_API_KEY_HERE' if not set
    data_service = DataService(api_key)
    datasets_response = data_service.get_datasets()
    if 'error' in datasets_response:
        logging.error(f"Error fetching datasets: {datasets_response}")
    else:
        logging.info(f"Available datasets: {json.dumps(datasets_response, indent=4)}")

class TestDataService(unittest.TestCase):
    @patch('requests.get')
    def test_get_datasets(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "fake data"}
        data_service = DataService(api_key="fake_api_key")
        response = data_service.get_datasets()
        self.assertEqual(response, {"data": "fake data"})

if __name__ == "__main__":
    main()
    unittest.main()
