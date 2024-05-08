import pandas as pd

def filter_data(data, filters):
    """ Filters a list of dictionaries based on given dictionary of filters where keys are properties.
    
    Args:
        data (list of dict): The data to filter.
        filters (dict): A dictionary where keys are the property names and values are the values to filter by.

    Returns:
        list of dict: The filtered data.
    """
    filtered_data = data
    for filter_key, filter_value in filters.items():
        filtered_data = [item for item in filtered_data if filter_key in item and item[filter_key] == filter_value]
    return filtered_data

def filtering(lst, condition):
    """ Filters a list based on a provided condition function.
    
    Args:
        lst (list): The list to filter.
        condition (function): A function that returns True for elements to include.

    Returns:
        list: The filtered list.
    """
    return [i for i in lst if condition(i)]

def filter_dataframe(df, column, value):
    """ Filters a pandas DataFrame based on the value of a column.
    
    Args:
        df (DataFrame): The DataFrame to filter.
        column (str): The column name to filter by.
        value: The value to filter the column by.

    Returns:
        DataFrame: The filtered DataFrame.
    """
    return df[df[column] == value]

def read_and_filter_csv(file_path, filter_column, filter_value):
    """
    Reads data from a CSV file and filters the DataFrame based on a specified column and value.
    
    Args:
        file_path (str): Path to the CSV file to read.
        filter_column (str): Column name to apply the filter on.
        filter_value: Value to filter the column by.
    
    Returns:
        DataFrame: A filtered pandas DataFrame.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Filter the DataFrame based on the specified column and value
    filtered_df = df[df[filter_column] == filter_value]

    return filtered_df


# Example usage:
data = [{"name": "John", "age": 25, "city": "New York"},
        {"name": "Alice", "age": 30, "city": "Los Angeles"},
        {"name": "Bob", "age": 25, "city": "New York"},
        {"name": "Eve", "age": 35, "city": "Los Angeles"}]

filters = {"age": 25, "city": "New York"}
print("Filtering list of dictionaries:")
print(filter_data(data, filters))

# Functional filtering example
print("\nFunctional filtering example:")
result = filtering(data, lambda x: x['city'] == 'Los Angeles' and x['age'] > 25)
print(result)

# Pandas DataFrame filtering example
# Assuming data.csv has the appropriate structure similar to the 'data' list
print("\nPandas DataFrame filtering example:")
df = pd.DataFrame(data)
filtered_df = filter_dataframe(df, 'age', 30)
print(filtered_df)

filtered_data_csv = read_and_filter_csv('data.csv', 'age', 30)
print(filtered_data_csv)