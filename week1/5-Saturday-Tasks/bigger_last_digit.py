n = input("Enter n: ")
m = input("Enter m: ")

n = int(n)
m = int(m)

lastDigit_n = n % 10
lastDigit_m = m % 10

if lastDigit_n > lastDigit_m:
    print(n)
elif lastDigit_n < lastDigit_m:
    print(m)
else:
    if n > m:
        print(n)
    else:
        print(m)
