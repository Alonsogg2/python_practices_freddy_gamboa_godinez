inputString = input("Enter list of number separared by space:")
inputString=inputString.split()
numbersList=[int(i) for i in inputString]
closeNumber=0
for num in numbersList[1:]:#skip the first element (using slicing)
    if(abs(num-numbersList[0])<abs(closeNumber-numbersList[0])):
        closeNumber=num

print(closeNumber)

