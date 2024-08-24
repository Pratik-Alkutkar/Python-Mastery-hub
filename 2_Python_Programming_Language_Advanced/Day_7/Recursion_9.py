"""
Date:- 27-04-2024
Code No:- 10
Code:- Write a program which accept one number from user and return its factorial. Eg. Input-5 Output-120 
"""

i = 1
Fact = 1

def Factorial(No):
    global i
    global Fact

    if(No >= 1):
        Fact = Fact * No
        No = No - 1
        Factorial(No)

    return Fact


def main():
    print("Enter the Number: ")
    Value = int(input())

    Ret = Factorial(Value)

    print("Factorial is: ", Ret)

if __name__ == "__main__":
    main()
