listSquaredNumbers=list(range(1,4))#start 1 and stop 4

for number in listSquaredNumbers:
    i=listSquaredNumbers.index(number)
    listSquaredNumbers[i]=number**2
print(listSquaredNumbers)
