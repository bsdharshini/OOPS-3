from abc import ABC,abstractmethod

#should add ABC as inherited
class Base(ABC):
    
    #abstract method
    @abstractmethod
    def getValue(self):
        pass 
    #should not have any implementation
class Child(Base):
    def __init__(self,p):
        self.p = p

    # without using abstract method we will get error    
    def getValue(self):
        return 100*(self.p)
obj = Child(1000)
print(obj.getValue()) #100000

# obj1 = Base()
# print(obj1.getValue()) #throws error saying getValue is not defined