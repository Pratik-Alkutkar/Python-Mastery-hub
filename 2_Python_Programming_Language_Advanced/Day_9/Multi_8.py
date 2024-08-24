"""
Date:- 04-05-2024
Code No:- 6
Code:- Multi-Threading--> A program to ask user a number and then print that much number of Even and Odd number using Multithreading.
"""

import threading
import os

def EvenDisplay(No):
    print("List of Even Numbers: ")
    x = 2
    for i in range(No):
        print("Even: ", x)
        x = x + 2

def OddDisplay(No):
    print("List of Odd Numbers: ")
    x = 1
    for i in range(No):
        print("Odd: ", x)
        x = x + 2

def main():
    print("Enter Number: ")
    Value = int(input())

    p1 = threading.Thread(target = EvenDisplay, args = (Value,))
    p2 = threading.Thread(target = OddDisplay, args = (Value,))

    p1.start() #Process won't begin until start is called.
    p1.join() #It means joh paryant p1 sampat nahi toh paryant pudhe jaycha nahi.
     
    p2.start()
    p2.join()

    print("End of main process")

if __name__ == "__main__":
    main()