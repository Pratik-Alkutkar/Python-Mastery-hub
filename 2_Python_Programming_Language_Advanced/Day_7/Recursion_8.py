"""
Date:- 27-04-2024
Code No:- 9
Code:- To take input from user and printing from that number to 1. i.e. reverse of Recursion_7.py
"""

i = 1

def DisplayR(No):
    global i

    if(No >= i):
        print(No)
        No = No - 1
        DisplayR(No)


def main():
    print("Enter the Number: ")
    Value = int(input())

    DisplayR(Value)

if __name__ == "__main__":
    main()