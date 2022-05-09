#Inherit exception class
class NegativeException(Exception):
    def __init__(self,value,message ="You have entered negative value"):
        self.value = value 
        self.message = message
    def __str__(self):
        return (f'{self.message} --> {self.value}')
class Age:
    def __init__(self,age):
        self.age =age
    def print_value(self):
        if self.age<0:
            raise NegativeException(self.age)
            # need to use raise to trigger negativeException
        else:
            print(self.age)
o = Age(-1)
o.print_value()

# o/p :  you have entered negative value --> -1
#   File "D:\Dharshini\Code\OOPS-3\d_custom_exception.py", line 13, in print_value
#     raise NegativeException(self.age)
#   File "D:\Dharshini\Code\OOPS-3\d_custom_exception.py", line 18, in <module>
#     o.print_value()

# if you dont want to print the whole error then make small change in above code

class Age1():
    def __init__(self,age):
        self.age =age
    def print_value(self):
        try: 
            if self.age<0:
                raise NegativeException(self.age)
                # need to use raise to trigger negativeException
            else:
                print(self.age)
        except NegativeException as e:
            print("Error:",e)
o = Age1(-1)
o.print_value()
#o/p: Error: You have entered negative value --> -1