"""
Date:- 04-05-2024
Code No:- 11
Code:- Multi-Core Programming -->  This program is executed on 'Single Core'.
"""

import os
import multiprocessing
import time

def Fun(No):
    Sum = 0
    print("PID is: ", os.getpid())
    for i in range(No):
        Sum = Sum + (No*No*No)

    return Sum

def main():
    starttime = time.time()
    Arr = [100000, 200000, 300000, 400000, 500000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000]
    Result = []

    for Value in Arr:
        Result.append(Fun(Value))

    print(Result)
    endtime = time.time()
    print("Time required for execution: ",endtime-starttime)
    
if __name__ == "__main__":
    main()