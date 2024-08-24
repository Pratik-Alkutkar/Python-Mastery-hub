"""
Date:- 20-04-2024
Code No:- 2
Code:- A program that executes by selection depending upon input. That is use of "if-else" for selection.
"""
print("Demonstration of SELLECTION")

Age = 0

print("Enter your Age: ")
Age = int(input())

if(Age<18):
    print("Sorry, You are not eligible for Voting!")
    
else:
    print("You can Vote!")

print("Thank you for using the Application.")