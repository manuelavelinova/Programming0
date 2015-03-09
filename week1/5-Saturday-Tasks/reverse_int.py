n = input("Enter n: ")
n = int(n)

newNumber = 0

while n != 0:
    digit = n % 10
    newNumber = newNumber * 10 + digit
    n = n //10

print("The new number is : " + str(newNumber))
