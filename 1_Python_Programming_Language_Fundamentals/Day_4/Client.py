"""
Date:- 14-04-2024
Code No:- 5
Code:- All Import. Importing a Module "Marvellous" that contains multiple fuctions "Addition, Substraction, Multiplication and Division".
After running this code a "__pycache__" folder got created in Session_4 folder that contains "Marvellous.pyc" file.
This method is always a "Good Programming Practice".
"""
import Marvellous

def main():
    print("Enter First Number: ")
    A = int(input())

    print("Enter Second Number: ")
    B = int(input())

    Ans = Marvellous.Addition(A,B)
    print("Addition is: ", Ans)

    Ans = Marvellous.Substraction(A,B)
    print("Substraction is: ", Ans)

    Ans = Marvellous.Multiplication(A,B)
    print("Multiplication is: ", Ans)

    Ans = Marvellous.Division(A,B)
    print("Division is: ", Ans)

main()