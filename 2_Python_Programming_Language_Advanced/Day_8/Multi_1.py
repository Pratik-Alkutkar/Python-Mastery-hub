"""
Date:- 28-04-2024
Code No:- 11
Code:- A program to check the PID of Running process and Parent process.
"""

import os

def main():
    print("PID of running process: ", os.getpid())
    print("PID of Parent process i.e. Command prompt is: ", os.getppid())

if __name__ == "__main__":
    main()