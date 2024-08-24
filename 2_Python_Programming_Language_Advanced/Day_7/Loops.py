"""
Date:- 27-04-2024
Code No:- 1
Code:- Print 1 to 5 using For and While Loop.
"""
def displayF():
    print("Inside Display of For Loop.")
    for i in range(1,6):
        print(i)

def displayW():
    print("Inside Display of While Loop.")
    No = 1
    while (No <= 5):
        print(No)
        No = No + 1

def main():
    displayF()
    displayW()

if __name__ == "__main__":
    main()