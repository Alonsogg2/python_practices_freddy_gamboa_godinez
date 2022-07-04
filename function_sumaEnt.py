numbersList=[3,1,34,5,5,2,4]

def sumEnt(numList):
    result=0
    for number in numList:
        result+=number
    return result

print(sumEnt(numbersList))