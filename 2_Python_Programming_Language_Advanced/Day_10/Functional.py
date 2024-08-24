"""
Date:- 05-05-2024
Code No:- 3
Code:- FUNCTIONAL PROGRAMMING--> Similar as Scripting, all runs on indentation level 0. But Functional programming is performed using Lambda functions. 
Accept 2 numbers from user and perform Addition and Subtraction.
"""
#Python supports Functional Programming

print("Demonstration of Functional")

Addition = lambda No1,No2 : No1 + No2

Subtraction = lambda No1, No2 : No1 - No2

def main():
    print("Enter First Number")
    A = int(input())

    print("Enter Second Number")
    B = int(input())

    Ret = Addition(A,B)
    print("Addition is: ",Ret)

    Ret = Subtraction(A,B)
    print("Subtraction is: ",Ret)

if __name__ == "__main__":
    main()