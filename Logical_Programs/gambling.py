#Simulates a gambler who start with $stake and place fair $1 bets until
#he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
#times he/she wins and the number of bets he/she makes.
import random
def gambling():
    win=0
    loose=0
    count=0
    stake=100
    goal=200
    while stake > 0 and stake < goal :
        num=random.randint(0,2)
        count+=1 #count the number of times
        if num==1:
            win+=1
            stake+=2
        elif num==0:
            loose+=1
            stake-=1 
            #calculating averages
        winAvg=(win/count)*100
        looseAvg=(loose/count)*100 
    print("win count :",win)
    print("Loose count :",loose)
    print("win Average :",winAvg)
    print("Loose Average :",looseAvg)
    print("cash remailning :",stake)
        
gambling()
