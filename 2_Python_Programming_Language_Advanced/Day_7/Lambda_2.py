"""
Date:- 27-04-2024
Code No:- 12
Code:- Using Lambda function and regular function perform addition.
"""
# Syntax-->
# Name = lambda Parameters : Logic
# Name(___, ___, .....)

def Addition(A,B):
    return A+B

Add = lambda A,B : A+B

def main():
    Ret = Addition(10,11)
    print("Addition is: ",Ret)

if __name__ == "__main__":
    main()