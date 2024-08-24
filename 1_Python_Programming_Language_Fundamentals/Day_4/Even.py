"""
Date:- 14-04-2024
Code No:- 11
Code:- To check whether a number is even or odd using if-else.
"""
def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even Number")
    else:
        print("It is Odd Number")

def main():
    print("Enter Number : ")
    A = int(input())

    CheckEven(A)

main()