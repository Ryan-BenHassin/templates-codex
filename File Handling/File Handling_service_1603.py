#TODO
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
