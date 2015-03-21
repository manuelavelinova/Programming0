p = input("Enter p : ")
p = int(p)

plusP = p + 2
minusP = p - 2

isPrime = True
start = 2

if p == 1:
    isPrime = False
while start < p :
    if p % start == 0:
        isPrime = False
        break
    start += 1

plusStart = 2
plusPrime = True

if plusP == 1:
    plusPrime = False
    
while plusStart < plusP:
    if plusP % plusStart == 0:
        plusPrime = False
        break
    plusStart += 1


minusStart = 2
minusPrime = True

if minusP == 1:
    minusPrime = False
    
while minusStart < minusP :
    if minusP % minusStart == 0:
        minusPrime = False
        break
    minusStart += 1

if isPrime and minusPrime and plusPrime:
    print(str(minusP), str(p) , str(plusP))
elif isPrime and minusPrime and (not plusPrime):
    print(str(minusP), str(p))
elif isPrime and plusPrime and  (not minusPrime):
    print(str(p), str(plusP))
elif not isPrime:
    print(str(p) + " is not prime number")
        
