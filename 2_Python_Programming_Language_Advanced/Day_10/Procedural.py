"""
Date:- 05-05-2024
Code No:- 2
Code:- PROCEDURAL PROGRAMMING--> In this type of programming, we define functions using 'def' keyword. Everything is separately defined, Addition, Subtraction, main and starter. 
Accept 2 numbers from user and perform Addition and Subtraction.
"""
#Python supports Procedural Programming --> Always write Codes in Procedural Programming in Interviews.

print("Demonstration of Procedural")

def Addition(No1,No2):
    Ans = No1 + No2
    return Ans

def Subtraction(No1,No2):
    Ans = No1 - No2
    return Ans

def main():
    print("Enter First Number")
    A = int(input())

    print("Enter Second Number")
    B = int(input())

    Ret = Addition(A,B)
    print("Addition is: ",Ret)

    Ret = Subtraction(A,B)
    print("Subtraction is: ",Ret)

if __name__ == "__main__":
    main()