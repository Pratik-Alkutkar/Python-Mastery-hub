"""
Date:- 28-04-2024
Code No:- 12
Code:- Getting PIDs of multiple processes.
"""

import os
import multiprocessing

def Task1(No):
    print("Executing First Task")
    print("PID of Task 1: ", os.getpid())
    print("PPID of Task 1: ", os.getppid())

def Task2(No):
    print("Executing Second Task")
    print("PID of Task 2: ", os.getpid())
    print("PPID of Task 2: ", os.getppid())

def main():
    print("PID of running process: ", os.getpid())
    print("PID of Parent process i.e. Command prompt is: ", os.getppid())

    Value = 11
    p1 = multiprocessing.Process(target = Task1, args=(Value, ))
    p2 = multiprocessing.Process(target = Task2, args=(Value, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()