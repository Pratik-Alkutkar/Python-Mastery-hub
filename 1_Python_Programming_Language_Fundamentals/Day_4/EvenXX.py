"""
Date:- 14-04-2024
Code No:- 14
Code:- We imported a module Even_Odd in "EvenXX.py" . We will write this type of code in "Interview".
"""
import Even_Odd

def main():
    print("Enter Number : ")
    A = int(input())

    Even_Odd.CheckEven(A)

#Starter
if __name__ == "__main__":  #This syntax is best practice and is used in Industry level programming.
    main()