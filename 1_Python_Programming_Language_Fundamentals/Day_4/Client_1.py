"""
Date:- 14-04-2024
Code No:- 6
Code:- Specific Import. From Marvellous we only imported Addition and Multiplication Functions only.
"""
from Marvellous import Addition
from Marvellous import Multiplication

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