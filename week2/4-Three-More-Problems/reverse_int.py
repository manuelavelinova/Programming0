n = input("Enter n: ")
n = int(n)

newDigit = 0 
while n != 0:
    digit = n % 10
    newDigit = (newDigit * 10) + digit
    n = n // 10
print("The reverse number is: " + str(newDigit))
    
