"""
Date:- 20-04-2024
Code No:- 7
Code:- Convert the Code No:- 6 in proper format. 
"""

def Display(Cnt):
    i = 0
    if(Cnt<=0):
        print("Invalid Input")
        return

    for i in range(Cnt):
        print("Jai Ganesh")

def main():
    print("Enter the Frequency: ")
    No = int(input())
    Display(No)

if __name__ == "__main__":
    main()