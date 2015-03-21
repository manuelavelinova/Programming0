n = input("Enter n : ")
n = int(n)

m = input("Enter m: ")
m = int(m)

lastDigitN = n % 10
lastDigitM = m % 10

if lastDigitN > lastDigitM:
    print(n)
elif lastDigitN < lastDigitM:
    print(m)
else:
    if n > m:
        print(n)
    else:
        print(m)
