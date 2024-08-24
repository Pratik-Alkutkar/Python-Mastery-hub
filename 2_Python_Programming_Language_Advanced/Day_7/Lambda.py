"""
Date:- 27-04-2024
Code No:- 11
Code:- Lambda Function- Mothya goshti la Chota karna, but it is not possible for all. To define Lambda function we use lambda keyword.
Limitation of Lambda Function:-
1) You can pass any number of parameters
1) The Function body should be written in one single line.
2) We cannot shift to another line while using Lamdda function.
"""

# "LAMBDA" is an important concept for Interview purpose.

#Regular Function
def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans

def main():
    Ret = Addition(10,11)
    print("Addition is: ",Ret)

if __name__ == "__main__":
    main()