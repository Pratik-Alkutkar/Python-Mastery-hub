"""
Date:- 04-05-2024
Code No:- 7
Code:- Multi-Core Programming --> Program to check number of Cores available on CPU.
"""

import multiprocessing

def main():
    print("Number of Cores: ", multiprocessing.cpu_count())

if __name__ == "__main__":
    main()