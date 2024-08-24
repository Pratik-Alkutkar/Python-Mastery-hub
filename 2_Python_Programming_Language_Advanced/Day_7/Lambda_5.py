"""
Date:- 27-04-2024
Code No:- 15
Code:- Take input from user and determine whether the number is Even or Odd using regular and lambda function.
"""

#Lambda Function
def CheckEven(A):
    return(A%2 == 0)

Check = lambda A : (A%2 == 0) 

def main():
    Ret = CheckEven(10)
    if(Ret == True):
        print("Its an Even number")
    else:
        print("Its an Odd number")

if __name__ == "__main__":
    main()