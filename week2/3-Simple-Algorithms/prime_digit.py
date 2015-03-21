n = input("Enter n: ")
n = int(n)

hasPrime = False
digits = []

while n != 0:
    digit = n % 10
    digits += [digit]
    n = n // 10


for digit in digits:
    if digit in [2,3,5,7]:
        hasPrime = True
        break
if hasPrime:
    print("True")
else:
    print("False")
    
        
    
        

