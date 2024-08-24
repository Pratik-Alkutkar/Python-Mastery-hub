"""
Date:- 11-05-2024
Code No:- 5
Code:- Exception Handling--> Finally keyword. 
"""
#Writing Finally block is optional. By deafult the program flow goes to 'finally' block though there is exception or not.

def main():
    Ans = 0

    try:
        print("Enter First number: ")
        No1 = int(input())

        print("Enter Second number: ")
        No2 = int(input())

        Ans = No1 / No2
 
    except ZeroDivisionError as zobj:   
        print("Exception occurred ",zobj)

    except ValueError as vobj:   
        print("Exception occurred ", vobj)

    except Exception  as eobj:       
        print ("Exception occurred: ", eobj)

    finally:
        print("Inside Finally Block")

    print("Division is: ",Ans)

if __name__ == "__main__":
    main()