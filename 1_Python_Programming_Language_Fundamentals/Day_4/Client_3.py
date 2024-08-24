"""
Date:- 14-04-2024
Code No:- 8
Code:- Here we used alias i.e. Toppan nav/Pet name for Marvellous, to avoid always writing whole word "Marvellous" instead we wrote "M", Eg:- M.Addition 
"""
import Marvellous as M

def main():
    print("Enter First Number: ")
    A = int(input())

    print("Enter Second Number: ")
    B = int(input())

    Ans = M.Addition(A,B)
    print("Addition is: ", Ans)

    Ans = M.Multiplication(A,B)
    print("Multiplication is: ", Ans)

main()