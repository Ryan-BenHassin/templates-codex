def validate_data(data, schema):
 import jsonschema
 try:
 jsonschema.validate(instance=data, schema=schema)
 return True
 except jsonschema.exceptions.ValidationError as err:
 return False

def main():
 data = {"name": "John", "age": 30}
 schema = {
 "type": "object",
 "properties": {
 "name": {"type": "string"},
 "age": {"type": "integer"}
 },
 "required": ["name", "age"]
 }
 if validate_data(data, schema):
 print("Data is valid")
 else:
 print("Data is not valid")

if __name__ == "__main__":
 main()
