"""
Date:- 13-04-2024
Code No:- 3
Code:- By default Python considers an input() to be a String. This means that if you input a number or any other type of data, Python will treat it as a string.
"""

print("Enter First number: ")
No1 = input()
print(type(No1))

print("Enter Second number: ")
No2 = input()
print(type(No2))

Ans = No1 + No2
print("Addition is: "+Ans)
print(type(Ans))