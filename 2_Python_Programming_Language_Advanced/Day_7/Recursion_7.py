"""
Date:- 27-04-2024
Code No:- 8
Code:- To take input from user and printing numbers from 1 to that number.
"""

i = 1

def DisplayR(No):
    global i

    if(i <= No):
        print(i)
        i = i + 1
        DisplayR(No)


def main():
    print("Enter the Number: ")
    Value = int(input())

    DisplayR(Value)

if __name__ == "__main__":
    main()