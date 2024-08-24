"""
Date:- 11-05-2024
Code No:- 3
Code:- Exception Handling (Specific and Generic Exception Handler). 
"""
#Generic Exception Handler is like pain killer tablet, one tablet for all tooth pain, back pain, headache, fracture.
#Specific Exception Handler is like going to specialized person like going to Dentist if Tooth is paining, going to physio for back pain, going to family doctor for headache, going to orthopedic doctor if fractured.

def main():
    Ans = 0

    try:
        print("Enter First number: ")
        No1 = int(input())

        print("Enter Second number: ")
        No2 = int(input())

        Ans = No1 / No2

#-->This is specific Exception Handler. 
    except ZeroDivisionError as zobj:    #This is Slip man 1 in Cricket
        print("Exception occurred ",zobj)

    except ValueError as vobj:    #This is Slip man 2 in Cricket, if 1 st does not catch the ball 2nd man catches it 
        print("Exception occurred ", vobj)

#-->This is Generic Exception Handler and must be always written at the bottom of code.
    except Exception  as eobj:      #This is M.S.Dhoni, no need of any slip he can individually catch all.
        print ("Exception occurred: ", eobj)

    print("Division is: ",Ans)

if __name__ == "__main__":
    main()