"""
Date:- 07-04-2024
Code No:- 3
Code:- Abnormal things we can do in Python with Variables.
"""
#We can assign multiple values to a single Variable. But, previous value gets overwritten/erased.
X = 11
print(type(X))

X = 89.75
print(type(X))

X = 'Python'
print(type(X))

X = False
print(type(X))

X = 87j
print(type(X))

#We can assign a single value to multiple Variables in following ways (Disclaimer:- Not a good programming practice).
A=B=C=11
print(A)
print(B)
print(C)

P,Q,R = 10,20,30
print(P)
print(Q)
print(R)