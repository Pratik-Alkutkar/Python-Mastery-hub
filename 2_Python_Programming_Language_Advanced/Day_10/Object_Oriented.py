"""
Date:- 05-05-2024
Code No:- 4
Code:- OBJECT ORIENTED PROGRAMMING-->
Accept 2 numbers from user and perform Addition and Subtraction.

--> Why OOP is used in Companies?
I] The project can be build in team. Each member can write his own class and then the classes can be merged together.
II] Experienced Developers demand for opting this technique as they grant everyone knows this programming technique even though they are from diiferent coding language background.
III] Object Oriented Programmed projects are more manageable, easy to maintain and are extensible.
"""
#Python supports Object Oriented Programming --> Never write Codes in Object Oriented Programming in Interviews.

print("Demonstration of Object Orientation")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Arithmetic:      # 'class' keyword is used to define the Class. Arithmetic is name of the class.
    def __init__(self, Value1, Value2):       # '__init__()' is Constructor which gets called when object is created.
        self.No1 = Value1       # Characteristics--> In simple words it is Data.
        self.No2 = Value2       # Characteristics--> In simple words it is Data.  

    def Addition(self):          # Behaviour--> Basically it is a Function.
        Ans = self.No1 + self.No2
        return Ans
    
    def Subtraction(self):       # Behaviour--> Basically it is a Function.
        Ans = self.No1 - self.No2
        return Ans

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Enter First Number")
A = int(input())

print("Enter Second Number")
B = int(input())

obj = Arithmetic(A,B)       # Object of a Class, constructor will be called using this.

Ret = obj.Addition()
print("Addition is: ",Ret)

Ret = obj.Subtraction()
print("Subtraction is: ",Ret)