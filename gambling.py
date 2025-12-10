import random






money=10000
currentDeposit=1

cycles=0

deposites =[]

while money>0:
    cycles+=1
    money-=currentDeposit
    if random.randint(0,1)==1:
        money+=currentDeposit*2
        currentDeposit=1
        print("win, money:\t",money,"currentDeposit:\t",currentDeposit)
    else:
        currentDeposit=2*currentDeposit
        print("loss, money:\t",money,"currentDeposit:\t",currentDeposit)
    
    if money>30000:
        money-=10000
        deposites.append(10000)

print(cycles)    
print(deposites)