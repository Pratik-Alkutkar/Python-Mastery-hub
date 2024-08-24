"""
Date:- 28-04-2024
Code No:- 10
Code:- Take input List from user and perform Filter, Map and Reduce. From list, filter out Even numbers, in map add 1 to each filtered element, to reduce add all mapped elements. 
Write the code using "Lambda function". Using FMR_Module 
"""

from FMR_Module import *

def main():
    print("Enter the number of Elements: ")
    n = int(input())
    Data = []
    for i in range(n):
        print("Enter the Number: ", i+1)
        Data.append(int(input()))

    FData = list(filterX(CheckEven,Data)) # FILTER
    print("Data after Filter activity: ", FData)

    MData = list(mapX(Increase, FData)) # MAP
    print("Data after Map activity: ", MData)

    RData = reduceX(Add, MData) # REDUCE
    print("Data after Reduce activity is: ", RData)

if __name__ == "__main__":
    main()