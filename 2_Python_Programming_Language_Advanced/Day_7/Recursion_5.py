"""
Date:- 27-04-2024
Code No:- 6
Code:- Recusrion- Printing from number 1 to Recursive Limit.
"""
i = 1

def fun():
    global i
    print("Inside fun", i)
    i = i + 1
    fun()

def main():
    fun()

if __name__ == "__main__":
    main()