"""
Date:- 21-04-2024
Code No:- 6
Code:- Accept elements from user and place them in List and add all elements in List.
"""
def Addition(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum


def main():
    print("Enter number of elements that you want to insert in the List: ")
    size = int(input())

    Arr = list() #Created Empty List

    print("Enter the Elements: ")

    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("The Elements in List are: ", Arr)
    
    Result = Addition(Arr)
    print("Summation of all Elements: ", Result)

if __name__ == "__main__":
    main()