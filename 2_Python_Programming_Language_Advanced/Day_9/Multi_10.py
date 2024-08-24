"""
Date:- 04-05-2024
Code No:- 8
Code:- Multi-Core Programming --> This program is executed on only 'One Core'. 
"""

import os

def Cube(No):
    print("PID is: ", os.getpid())
    return No*No*No

def main():
    print("PID is: ", os.getpid())
    Arr = [10, 20, 30, 40]
    Result = []

    for Value in Arr:
        Result.append(Cube(Value))

    print(Result)
    
if __name__ == "__main__":
    main()