#TODO
import os

class FileHandling:
 def __init__(self, file_path):
 self.file_path = file_path

 def read_file(self):
 try:
 with open(self.file_path, 'r') as file:
 return file.read()
 except FileNotFoundError:
 return "File not found"

 def write_file(self, content):
 try:
 with open(self.file_path, 'w') as file:
 file.write(content)
 return "File written successfully"
 except Exception as e:
 return str(e)

 def delete_file(self):
 try:
 os.remove(self.file_path)
 return "File deleted successfully"
 except FileNotFoundError:
 return "File not found"
 except Exception as e:
 return str(e)

 def copy_file(self, destination):
 try:
 with open(self.file_path, 'r') as file:
 content = file.read()
 with open(destination, 'w') as file:
 file.write(content)
 return "File copied successfully"
 except FileNotFoundError:
 return "File not found"
 except Exception as e:
 return str(e)

 def move_file(self, destination):
 try:
 os.rename(self.file_path, destination)
 return "File moved successfully"
 except FileNotFoundError:
 return "File not found"
 except Exception as e:
 return str(e)

 def file_exists(self):
 return os.path.exists(self.file_path)
