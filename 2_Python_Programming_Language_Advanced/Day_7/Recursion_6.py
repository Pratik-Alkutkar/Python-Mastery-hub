"""
Date:- 27-04-2024
Code No:- 7
Code:- Display 1 to 5.
"""
i = 1

def DisplayR():
    global i

    if(i <= 5):
        print(i)
        i = i + 1
        DisplayR()


def main():
    DisplayR()

if __name__ == "__main__":
    main()