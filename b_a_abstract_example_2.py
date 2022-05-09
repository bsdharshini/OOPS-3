from abc import ABC,abstractmethod
class Reader(ABC):
    def __init__(self,filename,path1):
        self.filename =filename
        self.path1 = path1
    #while creating obj must pass all this instance attr value

    @abstractmethod
    def get_filename(self):
        pass
    @abstractmethod
    def get_path1(self):
        pass
    # must use these 2 methods in subclass

class SubReader(Reader):
    # we can or cannot use init. But if we use then we need to add both the instance attr
    def get_filename(self):
        return self.filename
    def get_path1(self):
        return self.path1
    # no need to use super() to get parent class attr. Since abstract enforece child class to use attr

obj = SubReader("Hello","c\download")
print(obj.get_filename())
print(obj.get_path1())