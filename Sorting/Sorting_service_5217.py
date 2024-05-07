#TODO
def sort_service(input_type, input_data):
 if input_type == "asc":
 return sorted(input_data)
 elif input_type == "desc":
 return sorted(input_data, reverse=True)
 else:
 return "Invalid input type. Please choose 'asc' or 'desc'."

input_data = [64, 34, 25, 12, 22, 11, 90]
print(sort_service("asc", input_data))
print(sort_service("desc", input_data))
