class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            return str(e)

    def write_file(self, content):
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
            return "File written successfully"
        except Exception as e:
            return str(e)

    def append_file(self, content):
        try:
            with open(self.file_path, 'a') as file:
                file.write(content)
            return "File appended successfully"
        except Exception as e:
            return str(e)

    def delete_file(self):
        try:
            import os
            os.remove(self.file_path)
            return "File deleted successfully"
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            return str(e)

# Example usage:
file_handler = FileHandler('example.txt')
print(file_handler.read_file())
file_handler.write_file('Hello, World!')
print(file_handler.read_file())
file_handler.append_file(' Append this line!')
print(file_handler.read_file())
print(file_handler.delete_file())