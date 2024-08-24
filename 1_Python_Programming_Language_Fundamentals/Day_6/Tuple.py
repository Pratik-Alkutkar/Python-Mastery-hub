"""
Date:- 21-04-2024
Code No:- 7
Code:- Sequential Datatype --> TUPLE
# Tuple is faster than List because it is immutable. When we do not want to modify the elements in Future we use Tuple, 
whereas if we want to change or modify the elements in future we must use List.
"""

#--> TUPLE DATATYPE
#Hetereogeneous
#Ordered
#Indexed
#Immutable i.e. we cannot change the elements
#Allows Duplicate

Arr = (11, 18.90, True, "Pratik", 11)

print(type(Arr))
print(len(Arr))
print(Arr[0])
print(Arr[2])

Arr[0] = 21
print(Arr[0])