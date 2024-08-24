"""
Date:- 20-04-2024
Code No:- 10
Code:- Understanding the concepts of Function Arguements.
Types of Function Arguements -->
# 1: Positional Arguements
# 2: Keyword Arguements
# 3: Default Arguements
# 4: Variable number of Arguements
"""


def Information(Name, Age, Salary): #Name, Age, Salary are parameters.
    print("Name is: ", Name)
    print("Age is: ", Age)
    print("Salary is: ", Salary)

# Positional Arguements--> Everything is mapped to parameters as per the positions of parameters in def function.
Information("Amit", 32, 90000)
Information("Pratik", 21, 100000)
Information(69, "Ganpat", 100000) #Python blindly maps the parameters. So, here Name is 69, Age is Ganpat and Salary is 100000. Which is wrong and horrible.

# Keyword Arguements--> In this all paramters defined in def function must be known.
Information(Age=31, Salary=50000, Name="Rahul")