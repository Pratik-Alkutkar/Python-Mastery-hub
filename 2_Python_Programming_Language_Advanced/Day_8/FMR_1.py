"""
Date:- 28-04-2024
Code No:- 1
Code:- Take a hard coded List and perform Filter, Map and Reduce. From list, filter out Even numbers, in map add 1 to each filtered element, to reduce add all mapped elements.
"""
#-->Rules of FMR
#Filter function only takes Boolean values as input
#Map function takes 1 input and gives 1 output
#Reduce function takes 2 inputs and returns 1 output

from functools import reduce #Sagle functions tools swaroopat dilet, thus named functools.

def CheckEven(No):
    return(No % 2 == 0)

def Increase(No):
    return No + 1

def Add(A, B):
    return A + B

def main():
    Data = [11, 14, 20, 23, 18, 16, 15, 20]
    print("Data from input list: ", Data)

    FData = list(filter(CheckEven,Data)) # FILTER
    print("Data after Filter activity: ", FData)

    MData = list(map(Increase, FData)) # MAP
    print("Data after Map activity: ", MData)

#How Add worked in Reduce
# 15, 21, 19, 17, 21 
# 0 + 15 --> 15
# 15 + 21 --> 36
# 36 + 19 --> 55
# 55 + 17 --> 72
# 72 + 21 --> 93

    RData = reduce(Add, MData) # REDUCE
    print("Data after Reduce activity is: ", RData)

if __name__ == "__main__":
    main()