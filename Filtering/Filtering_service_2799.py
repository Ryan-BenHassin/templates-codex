def filter_data(data, filters):
 filtered_data = data
 for filter_key, filter_value in filters.items():
 filtered_data = [item for item in filtered_data if filter_key in item and item[filter_key] == filter_value]
 return filtered_data

data = [{"name": "John", "age": 25, "city": "New York"},
 {"name": "Alice", "age": 30, "city": "Los Angeles"},
 {"name": "Bob", "age": 25, "city": "New York"},
 {"name": "Eve", "age": 35, "city": "Los Angeles"}]

filters = {"age": 25, "city": "New York"}
print(filter_data(data, filters))
