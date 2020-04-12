import random
import pandas as pd
import numpy as np








def assign(num):         #Function for assigning choice according to the choice no.
    if num == 1:
        choice = 'ROCK'
    elif num == 2:

        choice = 'PAPER'
    elif num==3:
        choice = 'SCISSOR'
    return(choice)

def result(user,comp):   #Function for calculating result
    if ((user == 1 and  comp== 2) or (user == 2 and comp == 1)):
        print("paper wins => ", end="")
        return(2)

    elif ((user == 1 and comp== 3) or (user == 3 and comp== 1)):
        print("Rock wins =>", end="")
        return(1)
    else:
        print("scissor wins =>", end="")
        return(3)


print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")


n=int(input("how many rounds?\n"))
i=0
round_score = []
while(i!=n):
    print("\n\n\n*******ROUND-"+str(i+1)+" *******\n\n\n")  #For displaying which round is running.
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
    user_choice=int(input("User turn:-\t"))

    while (user_choice > 3) or (user_choice < 1):
        choice = int(input("enter valid input:-\t "))

    comp_choice=random.randint(1,3)


    while comp_choice==user_choice:
        comp_choice = random.randint(1, 3)

    user_choice_name=assign(user_choice)
    comp_choice_name=assign(comp_choice)

    print("\n\nuser choice is: " + user_choice_name)
    print("computer choice is: " + comp_choice_name)

    print("**** "+user_choice_name+" V/S "+comp_choice_name+" ****")
    winner= result(user_choice,comp_choice)

    if(winner==user_choice):
        print("*******YOU WIN*********\n\n")
        round_score.append([i+1,1,0])        #Score updating in list
    else:
        print("*******YOU LOSE*********\n\n")
        round_score.append([i+1,0,1])
    i=i+1
print("#*#*#*#*#*#*#* SCORE-TABLE *#*#*#*#*#*#*#")
df = pd.DataFrame(np.array(round_score), columns=['ROUND', 'USER_SCORE', 'COMP_SCORE'])  #Score table
print(df)
print("*$*$*$*$*$ TOTAL-SCORE $*$*$*$*$*$*")
print(df[["USER_SCORE","COMP_SCORE"]].sum())
