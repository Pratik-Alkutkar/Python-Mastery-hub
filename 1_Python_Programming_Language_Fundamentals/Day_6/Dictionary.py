"""
Date:- 21-04-2024
Code No:- 9
Code:- Sequential Datatype --> DICTIONARY
"""

# Duplicate Values are allowed and Duplicate Keys are not allowed. The previous value of key gets erased and new value is overwritten.

print("Demonstration of Dictionary")

Price = {"Python" : 2000, "Java" : 1500, "C" : 1100, "C++" : 3000, "Java" : 4300}
print(Price)

print(type(Price))

print(Price["C"]) #It will return the price of C i.e. 1100

print(Price.keys()) #To print Keys

print(Price.values()) #To print Values