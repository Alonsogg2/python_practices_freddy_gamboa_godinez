import random
randomList = []
evenList = []
oddList = []
#generate the randomList
for i in range(0,random.randint(1,30)):
    n = random.randint(1,30)
    randomList.append(n)
print(randomList)

#generate odd and even numbers list
for number in randomList:
    if(number%2==0):
        evenList.append(number)
    else:
        oddList.append(number)

print(evenList)
print(oddList)