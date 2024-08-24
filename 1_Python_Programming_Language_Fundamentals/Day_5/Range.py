"""
Date:- 20-04-2024
Code No:- 3
Code:- Demonstartion of Range function. Range is an in-built function provided by Python. Range only accepts Integer Values.
"""
# range(start, end, displacement)
# Start is by default 0 if not mentioned.
# Displacement is by default 1 if not mentioned.
# End should br mentioned by explicitely (It gets excluded).

# Displacement can also be negative which results in decrement or traverses in backward direction. In this scenario start and end points must be carefully given.

print(list(range(5))) #Range

print(list(range(3,8))) #Range with (start, end)

print(list(range(3,12,2))) #Range with (start, end, displacement)

print(list(range(20,1,-1))) #Range with negative displacement