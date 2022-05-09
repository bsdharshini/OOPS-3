class o:
    def __init__(self,price):
        self.price = price
    def getPrice(self):
        try:
            print(self.price + 100, ' ', 1/self.price )
        # except TypeError:
        #     print(int(self.price)+100, ' ', 1/int(self.price) )
        # except ZeroDivisionError:
        #     print(int(self.price)+100, ' ', 1)
        #nested exception
        except TypeError:
            try: 
                print(int(self.price)+100, ' ', 1/int(self.price) )
            except ZeroDivisionError:
                print(int(self.price)+100, ' ', 1)
            except:
                print("Exception occured")


obj = o('10') #'hello' -> Exception occured
obj.getPrice()

