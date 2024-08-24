"""
Date:- 27-04-2024
Code No:- 14
Code:- Take input from user and determine whether the number is Even or Odd using regular and lambda function.
"""

#Regular Function
def CheckEven(A):
    if(A%2 == 0):
        return True
    else:
        return False
    
def main():
    Ret = CheckEven(10)
    if(Ret == True):
        print("Its an Even number")
    else:
        print("Its an Odd number")

if __name__ == "__main__":
    main()