"""
Date:- 21-04-2024
Code No:- 8
Code:- Sequential Datatype --> SET
"""
#--> SET DATATYPE
#Hetereogeneous
#Unordered
#Unindexed
#Mutable i.e. we can change the elements
#Duplicate is not allowed

Arr = {11, 78.50, True, "Pratik", 11}
print(Arr)
print(len(Arr))

# print(Arr[0]) TypeError: 'set' object is not subscriptable

Arr.add("Python")
print(Arr)

Arr.remove("Python")
print(Arr)