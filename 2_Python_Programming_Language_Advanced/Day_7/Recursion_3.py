"""
Date:- 27-04-2024
Code No:- 4
Code:- How Recusrion works:- The "Inside fun" might be displayed close to 1000 times. Recursive function ends abruptly alfter close to almost 1000 recursion.
"""

def fun():
    print("Inside fun")
    fun()

def main():
    fun()

if __name__ == "__main__":
    main()