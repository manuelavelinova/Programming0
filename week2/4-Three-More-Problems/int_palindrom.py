n = input("Enter n : ")
n = int(n)

newDigit = 0
nonReversed =  n 
while n != 0:
    digit = n % 10
    newDigit = (newDigit * 10) + digit
    n = n // 10
    
if newDigit == nonReversed:
    print("The number is palindrom")
else:
    print("The number is not palndrom")
