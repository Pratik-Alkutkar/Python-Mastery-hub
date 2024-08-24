"""
Date:- 14-04-2024
Code No:- 2
Code:- Nested Functions, i.e. Defining Function inside another Function.
"""
def Calculations(No1, No2): #Mall
    def Addition(X, Y): #Addidas
        return X+Y 
    def Substraction(X, Y): #Nike
        return X-Y
    Ans1 = Addition(No1, No2)
    Ans2 = Substraction(No1,No2)
    return Ans1,Ans2 #2 Pishwya

print("Enter first number: ")
A = int(input())

print("Enter second number: ")
B = int(input())

Result1, Result2 = Calculations(A,B)

print("Addition is: ", Result1)
print("Substraction is: ", Result2)

#Flow = 15-->16-->17-->18-->19-->20-->21-->6-->11-->7-->8-->12-->9-->10-->13-->21-->23-->24