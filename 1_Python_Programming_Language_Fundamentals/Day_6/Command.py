"""
Date:- 21-04-2024
Code No:- 1
Code:- Demonstration of Command Line Argument.
"""

import sys

def main():
    print("Demonstration of Command Line Arguments")
    print("Name of Application: ",sys.argv[0])
    print("Datatype of argv is: ", type(sys.argv))
    print("Number of Command Line Arguments are: ",len(sys.argv))

if __name__ == "__main__":
    main()