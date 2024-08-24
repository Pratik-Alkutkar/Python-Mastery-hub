"""
Date:- 28-04-2024
Code No:- 4
Code:- Take a List from User and perform Filter, Map and Reduce. From list, filter out Even numbers, in map add 1 to each filtered element, to reduce add all mapped elements. 
Write the code using "Lambda function". 
"""

from functools import reduce

CheckEven = lambda No: No % 2 == 0

Increase = lambda No: No + 1

Add = lambda A, B: A + B

def main():
    print("Enter the number of Elements: ")
    n = int(input())
    Data = []
    for i in range(n):
        print("Enter the Number: ", i+1)
        Data.append(int(input()))

    FData = list(filter(CheckEven,Data)) # FILTER
    print("Data after Filter activity: ", FData)

    MData = list(map(Increase, FData)) # MAP
    print("Data after Map activity: ", MData)

    RData = reduce(Add, MData) # REDUCE
    print("Data after Reduce activity is: ", RData)

if __name__ == "__main__":
    main()