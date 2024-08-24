"""
Date:- 14-04-2024
Code No:- 10
Code:- In Python, the special variable "__name__" will display the name of its module i.e. Infosystems.
If only file is executable it will display '__main__' file
"""
import Infosystems

print("Inside User.py file")
print(__name__)

Infosystems.Display() #From here the flow will go to Display() function in Infosystems.py