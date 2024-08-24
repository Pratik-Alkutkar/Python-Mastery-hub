"""
Date:- 21-04-2024
Code No:- 2
Code:- To Add two numbers using Command Line Arguements
"""

import sys

def Addition(No1, No2):
    Ans = No1 + No2
    return Ans

def main():
    print("Welcome to the Application: "+sys.argv[0])

    if(len(sys.argv) != 3):
        print("Invalid number of arguements")
        print("Please provide 2 numeric arguments to perform addition")
        return

    Result = Addition(int(sys.argv[1]),int(sys.argv[2]))
    print("Addition is: ", Result)

if __name__ == "__main__":
    main()