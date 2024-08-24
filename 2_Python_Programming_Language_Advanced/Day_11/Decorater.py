"""
Date:- 11-05-2024
Code No:- 6
Code:- Decorater is a fancy concept in Python, not a necessity to learn but important for Interviews. 
"""
#Here the value of subtraction of 'small no. - large no.' is negative
#Pre-Defined function
def sub(A,B):
    print(A - B)

def main():
    No1 = int(input("Enter the First number: "))
    No2 = int(input("Enter the Second number: "))

    sub(No1, No2)

if __name__ == "__main__":
    main()