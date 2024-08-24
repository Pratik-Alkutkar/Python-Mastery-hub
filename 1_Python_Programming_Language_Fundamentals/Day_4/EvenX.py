"""
Date:- 14-04-2024
Code No:- 12
Code:- Updated version to check whether a number is even or odd using if-else.
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

#Starter
if __name__ == "__main__":  #This syntax is best practice and is used in Industry level programming.
    main()