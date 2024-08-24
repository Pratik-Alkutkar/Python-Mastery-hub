"""
Date:- 20-04-2024
Code No:- 12
Code:- Demonstration of Variable number of Arguements. In Variable number of arguements, we can pass multiple values for multiple number of parameters.
"""

def Addition(*No): #Here '*' indicates 'ANY'
    Ans = 0

    for i in No:
        Ans = Ans + i        
    return Ans

Result = Addition(10, 20, 30, 40, 50)
print(Result)