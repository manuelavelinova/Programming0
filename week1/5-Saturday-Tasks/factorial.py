n = input("Enter n: ")
n = int(n)

mult = 1

while n != 1:
    if n == 0:
        break
    else:
        mult = mult * n
        n = n - 1
print(mult)
