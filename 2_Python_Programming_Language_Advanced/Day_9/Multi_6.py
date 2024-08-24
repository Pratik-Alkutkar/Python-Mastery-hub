"""
Date:- 04-05-2024
Code No:- 4
Code:- A program to ask user a number and then print that much number of Even and Odd number and printing PIDs of processes.
"""

import multiprocessing
import os

def EvenDisplay(No):
    print("PID of Even process: ", os.getpid())
    print("List of Even Numbers: ")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2

def OddDisplay(No):
    print("PID of Odd process: ", os.getpid())
    print("List of Odd Numbers: ")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2

def main():
    print("PID of Main process: ", os.getpid())
    print("Enter Number: ")
    Value = int(input())

    p1 = multiprocessing.Process(target = EvenDisplay, args = (Value,))
    p2 = multiprocessing.Process(target = OddDisplay, args = (Value,))

    p1.start() #Process won't begin until start is called.
    p1.join() #It means joh paryant p1 sampat nahi toh paryant pudhe jaycha nahi.
    
    p2.start()
    p2.join()

    print("End of main process")

if __name__ == "__main__":
    main()