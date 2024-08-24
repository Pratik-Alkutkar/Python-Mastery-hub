"""
Date:- 20-04-2024
Code No:- 11
Code:- Demonstration of Default Arguement. If we do not pass a value to a parameter it will consider the default value of that parameter defined in def function.
Rules:- 
1) To use Default Arguements it should be written at the end of list.
"""

def Area(Radius, PI = 3.14): #Default Arguement is used for PI
    Result = PI * Radius * Radius
    return Result

Ans = Area(10.7) #If we do not mention value for parameter Pi, it will consider default value as 3.14 defined in def Area().
print("Area of Circle is: ", Ans)

Ans = Area(10.7, 7.20) #If we mention another value for parameter PI, default arguement/value won't be used.
print("Area of Circle is: ", Ans)