"""
Date:- 27-04-2024
Code No:- 13
Code:- Using Lambda function and regular function find the cube.
"""
# Syntax-->
# Name = lambda Parameters : Logic
# Name(___, ___, .....)

def Cube(A):
    return A*A*A

CubeX = lambda A : A*A*A

def main():
    Ret = CubeX(10)
    print("Cube is: ",Ret)

if __name__ == "__main__":
    main()