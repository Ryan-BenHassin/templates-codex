import os

class FileHandlingService:
    def __init__(self, base_path=''):
        self.base_path = base_path  # Allow setting of base path at initialization

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

    def copy_file(self, filename, destination):
        source_path = os.path.join(self.base_path, filename)
        destination_path = os.path.join(self.base_path, destination)
        try:
            with open(source_path, 'r') as file:
                content = file.read()
            with open(destination_path, 'w') as file:
                file.write(content)
            return "File copied successfully"
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            return str(e)

    def move_file(self, filename, destination):
        source_path = os.path.join(self.base_path, filename)
        destination_path = os.path.join(self.base_path, destination)
        try:
            os.rename(source_path, destination_path)
            return "File moved successfully"
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            return str(e)

    def file_exists(self, filename):
        file_path = os.path.join(self.base_path, filename)
        return os.path.exists(file_path)


# Set the base path if necessary
base_directory = ''  # Update this to your directory
file_service = FileHandlingService(base_directory)

# Test copying a file
file_service.create_file('example.txt', 'Hello World!')
copy_status = file_service.copy_file('example.txt', 'copy_of_example.txt')
print(copy_status)  # Should say "File copied successfully"

# Test if the file exists
exists = file_service.file_exists('copy_of_example.txt')
print("File exists:", exists)  # Should return True

# Test moving a file
move_status = file_service.move_file('copy_of_example.txt', 'moved_example.txt')
print(move_status)  # Should say "File moved successfully"

# Ensure the file was moved
exists_after_move = file_service.file_exists('copy_of_example.txt')
print("File exists after move:", exists_after_move)  # Should return False

delete_file= file_service.delete_file('moved_example.txt')
print("Attempted to delete file passed quietly.")