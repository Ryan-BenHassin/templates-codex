import pandas as pd

def data_transformation(file_path, column_names, transformation_rules):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path, names=column_names, header=None)

        # Apply transformation rules
        for column, transformation in transformation_rules.items():
            if transformation == 'lower':
                df[column] = df[column].apply(lambda x: x.lower())
            elif transformation == 'upper':
                df[column] = df[column].apply(lambda x: x.upper())
            elif transformation == 'strip':
                df[column] = df[column].apply(lambda x: x.strip())
            elif transformation == 'trim':
                df[column] = df[column].apply(lambda x: x.strip())
            elif transformation == 'remove_special_chars':
                df[column] = df[column].apply(lambda x: ''.join(e for e in x if e.isalnum()))
            elif transformation == 'remove_duplicates':
                df = df.drop_duplicates(subset=column, keep='first')

        return df
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
file_path = 'data.csv'
column_names = ['column1', 'column2', 'column3']
transformation_rules = {
    'column1': 'lower',
    'column2': 'upper',
    'column3': 'strip'
}

transformed_data = data_transformation(file_path, column_names, transformation_rules)
print(transformed_data)