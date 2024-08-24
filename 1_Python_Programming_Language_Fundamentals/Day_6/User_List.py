"""
Date:- 21-04-2024
Code No:- 5
Code:- Accept elements from user and place them in List.
"""

def main():
    print("Enter number of elements that you want to insert in the List: ")
    size = int(input())

    Arr = list()

    print("Enter the Elements: ")

    for i in range(size):
        no = int(input())
        Arr.append(no)
    print("The Elements in List are: ", Arr)

if __name__ == "__main__":
    main()