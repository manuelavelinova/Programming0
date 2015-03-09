n = input("Enter n: ")
n = int(n)

sameAsN = n
newNumber = 0
while n != 0:
    digit = n % 10
    newNumber = newNumber * 10 + digit
    n = n // 10
if newNumber != sameAsN:
    print("The number is not palindrom")
else:
    print("The number is   palindrom")
