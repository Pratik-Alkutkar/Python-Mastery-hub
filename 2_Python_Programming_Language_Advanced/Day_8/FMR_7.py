"""
Date:- 28-04-2024
Code No:- 7
Code:- Take a hard coded List and perform Filter, Map and Reduce. From list, filter out Even numbers, in map add 1 to each filtered element, to reduce add all mapped elements. 
Write the code using "Lambda function". Also writing User defined Filter, Map and Reduce function "filterX()" and "mapX()" and "reduceX()". 
"""

CheckEven = lambda No: No % 2 == 0
Increase = lambda No: No + 1
Add = lambda A, B: A + B

#Task:- Name of Function #Elements:- List of Data Elements

#   filterX(CheckEven, [11, 14, 20, 23, 18, 16, 15, 20])
def filterX(Task, Elements):
    Result = [] #Empty List to store filtered data

    for no in Elements:
        Ret = Task(no)
        if(Ret == True):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task, Elements):
    Sum = 0

    # [15, 21, 19, 17, 21]
    for no in Elements:
        Sum = Task(Sum,no)

    return Sum

def main():
    Data = [11, 14, 20, 23, 18, 16, 15, 20]
    print("Data from input list: ", Data)

    FData = list(filterX(CheckEven,Data)) # FILTER
    print("Data after Filter activity: ", FData)

    MData = list(mapX(Increase, FData)) # MAP
    print("Data after Map activity: ", MData)

    RData = reduceX(Add, MData) # REDUCE
    print("Data after Reduce activity is: ", RData)

if __name__ == "__main__":
    main()