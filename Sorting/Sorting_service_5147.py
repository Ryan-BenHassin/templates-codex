def sort_list(input_list, sort_type="asc"):
 if sort_type == "asc":
 return sorted(input_list)
 elif sort_type == "desc":
 return sorted(input_list, reverse=True)
 else:
 return "Invalid sort type. Please enter 'asc' for ascending or 'desc' for descending."

input_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", input_list)
print("Sorted list (Ascending order):", sort_list(input_list, "asc"))
print("Sorted list (Descending order):", sort_list(input_list, "desc"))
