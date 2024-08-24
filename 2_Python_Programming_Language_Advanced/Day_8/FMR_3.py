"""
Date:- 28-04-2024
Code No:- 3
Code:- Take a hard coded List and perform Filter, Map and Reduce. From list, filter out Even numbers, in map add 1 to each filtered element, to reduce add all mapped elements. 
Write the code using "Lambda function". + in this code use "Anonymous functions".
"""

from functools import reduce

def main():
    Data = [11, 14, 20, 23, 18, 16, 15, 20]
    print("Data from input list: ", Data)

    FData = list(filter((lambda No: No % 2 == 0),Data)) # FILTER
    print("Data after Filter activity: ", FData)

    MData = list(map((lambda No: No + 1), FData)) # MAP
    print("Data after Map activity: ", MData)

    RData = reduce((lambda A, B: A + B), MData) # REDUCE
    print("Data after Reduce activity is: ", RData)

if __name__ == "__main__":
    main()