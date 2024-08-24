"""
Date:- 05-05-2024
Code No:- 6
Code:- Demostrates Class Method and Static method.
"""
class Demo:
    Data1 = 11  #class variable
    Data2 = 21  #class variable

    def __init__(self, A, B):  #instance method
        print("Inside Constructor")
        self.No1 = A  #instance variable
        self.No2 = B  #instance variable

    def Display(self):  #instance method
        print("Value of No1 from display: ",self.No1)
        print("Value of No2 from display: ",self.No2)
        print("Value of Data1 from display: ",Demo.Data1)
        print("Value of Data2 from display: ",Demo.Data2)

    @classmethod  #Decorater- Fortuner varchi laal batti. Which makes it special Mantri's oR VIPs car.
    def Fun(cls): #Class method #Normal Fortuner which doesn't signify who the person is.
        print("Value of Data1 from Fun: ", Demo.Data1)
        print("Value of Data2 from Fun: ", Demo.Data2)

    @staticmethod
    def Gun(): #Static method
        print("Inside Static Method")

Demo.Fun()
Demo.Gun()
obj = Demo(5,10) 
obj.Display() 