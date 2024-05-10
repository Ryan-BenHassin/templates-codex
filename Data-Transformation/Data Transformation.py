import pandas as pd
import numpy as np

class DataTransformer:
    def __init__(self, data):
        self.data = data

    def rename_columns(self, columns_dict):
        self.data.rename(columns=columns_dict, inplace=True)

    def drop_columns(self, columns_list):
        self.data.drop(columns=columns_list, axis=1, inplace=True)

    def handle_missing_values(self, method):
        # Select numeric columns for mean and median methods
        numeric_columns = self.data.select_dtypes(include=[np.number])
        if method == 'mean':
            self.data.fillna(numeric_columns.mean(), inplace=True)
        elif method == 'median':
            self.data.fillna(numeric_columns.median(), inplace=True)
        elif method == 'mode':
            self.data.fillna(self.data.mode().iloc[0], inplace=True)
        else:
            self.data.fillna(method, inplace=True)  # Make sure 'method' is a valid fill value

    def transform_data_types(self, columns_dict):
        for column, data_type in columns_dict.items():
            if column in self.data.columns:  # Check if the column exists before transformation
                self.data[column] = self.data[column].astype(data_type)
            else:
                print(f"Warning: Column '{column}' not found in data.")

    def data_transformation(self, rename_dict, drop_list, missing_values_method, data_types_dict):
        self.rename_columns(rename_dict)
        self.drop_columns(drop_list)
        self.handle_missing_values(missing_values_method)
        self.transform_data_types(data_types_dict)
        return self.data

# Example test
# Ensure the column names and methods are correctly specified before running this
data = pd.read_csv('data.csv')
transformer = DataTransformer(data)
transformed_data = transformer.data_transformation(
    {'old_column_name': 'new_column_name'}, 
    ['column_to_drop'], 
    'mean',  # Corrected from 'ean' to 'mean'
    {'column_to_int': int, 'column_to_float': float}
)
print(transformed_data.head())
