import pandas as pd

def filter_data(df, column, value):
    return df[df[column] == value]

# Example usage:
df = pd.read_csv('data.csv')
filtered_df = filter_data(df, 'age', 30)
print(filtered_df)