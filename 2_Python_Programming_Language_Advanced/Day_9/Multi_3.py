"""
Date:- 04-05-2024
Code No:- 1
Code:- A program to ask user a number and then print that much number of Even and Odd number. 'It is Serial Programming'
"""

def EvenDisplay(No):
    print("List of Even Numbers: ")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2

def OddDisplay(No):
    print("List of Even Numbers: ")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2

def main():
    print("Enter Number: ")
    Value = int(input())

    EvenDisplay(Value)
    OddDisplay(Value)

if __name__ == "__main__":
    main()