"""
Date:- 14-04-2024
Code No:- 3
Code:- Writing main() function. A good programming practice. We simply create an Entry point function i.e. main().
"""
def Addition(No1, No2): #Dukan
    print("Inside Addition Function")
    Ans = No1 + No2
    return Ans #Fulancha Puda by Dukandar

def main(): #Ghar
    print("Inside Main Function")

    print("Enter First Number: ")
    A = int(input())

    print("Enter Second Number: ")
    B = int(input())

    Result = Addition(A,B) #Apan Fulancha Puda Pishwit(Result) ghetla

    print("Addition is: ", Result)

main() #Starter
print("End of Application")

#Flow= 24-->11-->12-->13-->14-->15-->16-->17-->18-->19-->20-->6-->7-->8-->9-->20-->21-->22-->25