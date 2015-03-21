n = input("Ener n: ")
n = int(n)

digits = []

while n!= 0:
    digit = n % 10
    digits += [digit]
    n = n // 10
print(digits)

middleNumber = 0
for digit in digits:
    middleNumber = middleNumber * 10 + digit
resultList = []

while middleNumber != 0:
    resDigit = middleNumber % 10
    resultList += [resDigit]
    middleNumber = middleNumber // 10

finalNumber = 0
for resDigit in resultList:
    finalNumber = finalNumber * 10 + resDigit
print(finalNumber)
    
