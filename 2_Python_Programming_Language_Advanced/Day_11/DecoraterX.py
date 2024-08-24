"""
Date:- 11-05-2024
Code No:- 7
Code:- Decorater is a fancy concept in Python, not a necessity to learn but important for Interviews. 
"""

#Here the value of subtraction of 'small no. - large no.' is now positive.

def sub(A,B):           #0x100
    print(A - B)

#SmartSub() is a user defined Decorater    
def SmartSub(fptr):      #0x200       #fptr stands for Function Pointer (Just named no such keyword)
    def Inner(A,B):      #0x300
        if A < B:
            A,B = B,A    #Values swapped
        return fptr(A,B)
    return Inner         # return 0x300

sub = SmartSub(sub)      # SmartSub(0x100)

def main():              #0x400
    No1 = int(input("Enter the First number: "))
    No2 = int(input("Enter the Second number: "))

    sub(No1, No2)        #0x300(1990, 1992)

if __name__ == "__main__":
    main()