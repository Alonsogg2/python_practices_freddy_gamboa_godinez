import random
randomList = []
reverseList=[]

#generate the randomList
for i in range(0,random.randint(1,30)):
    n = random.randint(1,30)
    randomList.append(n)
print(randomList)

reverseList=randomList
reverseList.reverse()
print(reverseList)
