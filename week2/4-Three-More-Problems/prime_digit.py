n = input("Enter n : ")
n = int(n)

digits = [] 
while n != 0:
    digit = n % 10
    digits += [digit]
    n = n // 10

print(digits)

isPrime = False

for digit in digits:
    if digit in [2,3,5,7]:
        isPrime = True
        break
if isPrime == True:
    print("Yes")
else:
    print("No")
