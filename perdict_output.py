#1
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def getValue(self):
        pass
    @abstractmethod
    def setValue(self):
        pass
a = A()
a.getValue() # Exception has occurred: TypeError Can't instantiate abstract class A with abstract method getValue

#2

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def getValue(self):
        print("A getValue")
    @abstractmethod
    def setValue(self):
        print("A setValue")
class B(A):
    
    def getValue(self):
        print("B getValue")
    
    def setValue(self):
        super().setValue()
o =B()
o.getValue()
o.setValue()