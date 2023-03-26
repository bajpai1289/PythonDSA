from abc import ABC, abstractmethod
from decimal import InvalidOperation

class Stream(ABC):  #we dont want this class to be called, it would be like a half baked cookie which 
    # will be completed by its deriverd classes to do that we nbeed the abstract base class
    def __init__(self) -> None:
        self.opened - False

    def open(self):
        if self.opened:
            raise InvalidOperation("Stream is already opened")
        self.opened=True
    def close(self):
        if not self.opened:
            return "stream not opened yet"
        self.opened=True
    #this method created to make the class methods abstract
    @abstractmethod
    def read(self):
        pass
    
class NetworkStream(Stream):
    def read(self):
        print("reading data from the stream")
    
stream=Stream()  #this will be resulting in the error
stream.open()
            