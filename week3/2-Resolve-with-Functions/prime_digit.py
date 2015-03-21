def is_prime(n):
    start = 2
    isPrime = True

    while start < n:
        if n % start == 0:
            isPrime = False
        if n == 1:
            isPrime = False
        start += 1

    if isPrime:
        return True
    else:
        return False

def to_digits(n):
    
    digits = []
    
    while n != 0:
        digit = n % 10
        digits += [digit]
        n = n // 10
    return digits

n = input("Enter n: ")
n = int(n)

result = to_digits(n)
primeDigit = False
    
for res in  result:
    if is_prime(res):
        primeDigit = True
        break
if primeDigit:
    print("There are prime digits")
        
else:
    print("There are no prime digits")
