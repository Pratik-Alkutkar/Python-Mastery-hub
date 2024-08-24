"""
Date:- 14-04-2024
Code No:- 7
Code:- Here from Marvellous we imported all Functions using *
"""
from Marvellous import *

def main():
    print("Enter First Number: ")
    A = int(input())

    print("Enter Second Number: ")
    B = int(input())

    Ans = Addition(A,B)
    print("Addition is: ", Ans)

    Ans = Multiplication(A,B)
    print("Multiplication is: ", Ans)

main()