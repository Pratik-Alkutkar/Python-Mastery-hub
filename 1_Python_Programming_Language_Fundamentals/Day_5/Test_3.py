"""
Date:- 20-04-2024
Code No:- 9
Code:- Convert Code No:- 8 into While loop
"""

def Display(Cnt):
    i = 0
    if(Cnt<=0):
        print("Invalid Input")
        return

    while(i<Cnt):
        print("Jai Ganesh")
        i = i + 1

def main():
    print("Enter the Frequency: ")
    No = int(input())
    Display(No)

if __name__ == "__main__":
    main()