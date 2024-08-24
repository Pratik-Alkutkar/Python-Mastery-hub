"""
Date:- 04-05-2024
Code No:- 10
Code:- Multi-Core Programming -->  This program is executed on 'Multiple Cores'. In Multi-core programming different processes are created and each process runs on different Core.
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
    Arr = [100000, 200000, 300000, 400000, 500000]
    Result = []

    p = multiprocessing.Pool()
    Result = p.map(Fun,Arr)
    p.close()
    p.join()

    print(Result)
    endtime = time.time()
    print("Time required for execution: ",endtime-starttime)
    
if __name__ == "__main__":
    main()