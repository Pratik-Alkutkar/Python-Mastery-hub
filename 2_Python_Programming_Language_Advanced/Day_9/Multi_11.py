"""
Date:- 04-05-2024
Code No:- 9
Code:- Multi-Core Programming -->  This program is executed on 'Multiple Cores'. In Multi-core programming different processes are created and each process runs on different Core.
"""

import os
import multiprocessing

def Cube(No):
    print("PID is: ", os.getpid())
    return No*No*No

def main():
    Arr = [10, 20, 30, 40]
    Result = []

    p = multiprocessing.Pool()
    Result = p.map(Cube,Arr)
    p.close()
    p.join()

    print(Result)
    
if __name__ == "__main__":
    main()