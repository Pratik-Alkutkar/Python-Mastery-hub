"""
Date:- 20-04-2024
Code No:- 8
Code:- To print multiple Jai Ganesh in same line and not on next line.
"""

def Display(Cnt):
    i = 0
    if(Cnt<=0):
        print("Invalid Input")
        return

    for i in range(Cnt):
        print("Jai Ganesh", end = " ") #To print number of Jai Ganesh on same Line.

def main():
    print("Enter the Frequency: ")
    No = int(input())
    Display(No)

if __name__ == "__main__":
    main()