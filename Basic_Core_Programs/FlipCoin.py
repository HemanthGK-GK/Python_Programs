
import random
def flipCoin(num):
    tailCount=0
    headCount=0
    for i in range(num):
        side=random.randint(1,2)
        if side==1:
            headCount += 1
        else:
            tailCount += 1
    headPercent=(headCount/num)*100
    tailPercent=(tailCount/num)*100

    print ("Heads percentage: "+str(headPercent))
    print ("Tails percentage: "+str(tailPercent))

flipCoin(10)
