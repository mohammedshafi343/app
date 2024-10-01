# file_manager.py
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self, data):
        with open(self.file_name, 'w') as file:
            file.write(data)

    def read_file(self):
        with open(self.file_name, 'r') as file:
            return file.read()

class AdvancedFileManager(FileManager):
    def append_to_file(self, data):
        with open(self.file_name, 'a') as file:
            file.write(data)

# Usage
file_manager = AdvancedFileManager("example.txt")
file_manager.write_file("Hello, this is the first line.\n")
file_manager.append_to_file("This is the second line.\n")
content = file_manager.read_file()
print(content)
