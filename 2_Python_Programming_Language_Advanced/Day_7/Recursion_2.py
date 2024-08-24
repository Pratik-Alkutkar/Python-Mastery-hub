"""
Date:- 27-04-2024
Code No:- 3
Code:- Changing the recursion limit.
"""

import sys

def main():
    print("Recursion Limit is: ", sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print("Recursion Limit is: ", sys.getrecursionlimit())

if __name__ == "__main__":
    main()