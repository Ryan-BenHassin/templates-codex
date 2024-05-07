import os

class FileHandlingService:
    def __init__(self):
        self.base_path = 'path_to_your_files'

    def create_file(self, filename, content):
        file_path = os.path.join(self.base_path, filename)
        with open(file_path, 'w') as f:
            f.write(content)

    def read_file(self, filename):
        file_path = os.path.join(self.base_path, filename)
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def update_file(self, filename, content):
        file_path = os.path.join(self.base_path, filename)
        try:
            with open(file_path, 'w') as f:
                f.write(content)
        except FileNotFoundError:
            return None

    def delete_file(self, filename):
        file_path = os.path.join(self.base_path, filename)
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass

# usage
file_service = FileHandlingService()
file_service.create_file('example.txt', 'Hello World!')
print(file_service.read_file('example.txt'))  # Output: Hello World!
file_service.update_file('example.txt', 'Hello Universe!')
print(file_service.read_file('example.txt'))  # Output: Hello Universe!
file_service.delete_file('example.txt')