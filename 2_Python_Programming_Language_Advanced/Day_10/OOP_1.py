"""
Date:- 05-05-2024
Code No:- 5
Code:- Explaining flow of Constructor. Also demostrates Instance method.
"""
#Example--> In a Thali Restaurant
class Demo:
    Data1 = 11 #Class Variable-Kanda,Limbu,Loncha Vati which is common between apan dogha.
    Data2 = 21 #Class Variable-Kanda,Limbu,Loncha Vati which is common between apan dogha.

    def __init__(self, A, B): #Pahile aleli rikami thali jyamadhe nustya vatya ni chamche ahet.
        print("Inside Constructor")
        self.No1 = A #Instance Variable - A
        self.No2 = B #Instance Variable - B

    def Display(self): #Instance Method
        print("Value of No1 from display: ",self.No1)
        print("Value of No2 from display: ",self.No2)
        print("Value of Data1 from display: ",Demo.Data1)
        print("Value of Data2 from display: ",Demo.Data2)

obj1 = Demo(5,10) #Majha Taat

obj2 = Demo(15,20) #Tumcha Taat

#No1, No2 are instance variable mhanje aplya taat madhle gulabjamun ani bhaji chi vati
#Jar majhi gulabjamun chi vati sampli it won't affect tumhala. i.e. no change in your gulabjamun vati

print("Value of No1 from obj1: ", obj1.No1)
print("Value of No2 from obj1: ", obj1.No2)

print("Value of No1 from obj2: ", obj2.No1)
print("Value of No2 from obj2: ", obj2.No2)

print("Value of Data1: ", Demo.Data1)
print("Value of Data2: ", Demo.Data2)

obj1.Display()
obj2.Display()