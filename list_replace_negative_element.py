numberList=[1,2,3,656,-151,781,-17,-17]

for number in numberList:
    if(number<0):
        i=numberList.index(number)
        numberList[i]=0

print(numberList)