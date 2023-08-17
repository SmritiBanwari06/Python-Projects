import random
def check(user,comp):
    if(user==comp): 
        return 0
    if(user ==0 and comp==1):
        return -1
    if(user ==1 and comp==2):
        return -1
    if(user==2 and comp==0):
        return -1
    return 1

comp = random.randint(0,2)
user = int(input("0 for Rock, 1 for Paper, 2 for Scissors: "))


print("YOU: ",user)
print("Computer: ", comp)


score = check(user,comp)
if(score==0):
    print("Its a DRAW!!")
elif(score==-1):
    print("Sorry you lose.Better luck next time.")
else:
    print("HURRAH!! YOU WON")