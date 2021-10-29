import random
def coupounNumber(Num):
    count=0
    list=[]
    for i in range(Num): 
        randomNum=random.randint(10,100)
        count+=1
        while randomNum in list:
            randomNum=random.randint(10,100)
            count+=1
        list.append(randomNum)
    print(list)
    print("The count is :",count)

Num =int(input("Enter a number :"))
coupounNumber(Num)