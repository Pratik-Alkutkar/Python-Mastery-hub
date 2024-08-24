"""
Date:- 27-04-2024
Code No:- 5
Code:- Recusrion for printing a value i. 
"""

def fun():
    i = 1
    print("Inside fun", i)
    i = i + 1
    fun()

def main():
    fun()

if __name__ == "__main__":
    main()