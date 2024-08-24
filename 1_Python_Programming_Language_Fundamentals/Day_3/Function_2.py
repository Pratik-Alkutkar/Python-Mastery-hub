"""
Date:- 13-04-2024
Code No:- 7
Code:- Workflow/Execution of Code Line by Line is 6-->10-->11-->13-->14-->16-->6-->7-->8-->18. 
"""
def Addition(No1, No2):
    Ans = No1 + No2
    return Ans

print("Enter First Number: ")
A = int(input())

print("Enter Second Number: ")
B = int(input())

Result = Addition(A,B)

print("Addition is: ", Result)