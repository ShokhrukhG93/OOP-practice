# Import ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod

# Define an abstract base class FileHandler
class FileHandler(ABC):
    # Abstract method read, which must be implemented by any subclass
    @abstractmethod
    def read(self, file_path):
        pass

    # Abstract method write, which must be implemented by any subclass
    @abstractmethod
    def write(self, file_path, data):
        pass


# Define a concrete class TextFileHandler inheriting from FileHandler
class TextFileHandler(FileHandler):
    # Implementation of the read abstract method
    def read(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    # Implementation of the write abstract method
    def write(self, file_path, data):
        with open(file_path, 'w') as file:
            file.write(data)


# Define a concrete class BinaryFileHandler inheriting from FileHandler
class BinaryFileHandler(FileHandler):
    # Implementation of the read abstract method
    def read(self, file_path):
        with open(file_path, 'rb') as file:
            return file.read()
    
    # Implementation of the write abstract method
    def write(self, file_path, data):
        with open(file_path, 'wb') as file:
            file.write(data)


# Using the abstract interface
# Create an instance of TextFileHandler and call write and read
text_handler = TextFileHandler()
text_handler.write('sample.txt', 'Hello, World!')
print(text_handler.read('sample.txt')) # Output: Hello, World!

# Create an instance of BinaryFileHandler and call write and read
binary_handler = BinaryFileHandler()
binary_handler.write('sample.bin', b'\x00\xFF')
print(binary_handler.read('sample.bin'))
