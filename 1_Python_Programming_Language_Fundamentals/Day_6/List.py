"""
Date:- 21-04-2024
Code No:- 3
Code:- Sequential Datatype --> LIST
"""
#--> LIST DATATYPE
#Hetereogeneous
#Ordered
#Indexed
#Mutable i.e. we can change the elements
#Allows Duplicate

Arr = [11, 78.50, True, "Pratik", 11]
print(Arr)

print("Length of List is: ", len(Arr))
print(Arr[3])

Arr[0] = 21
print(Arr)

Arr.append(51)
print(Arr)
print("Length of List is: ", len(Arr))
