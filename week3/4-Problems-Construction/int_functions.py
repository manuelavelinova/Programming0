def reverse_int(n):
    newN = 0
    while n != 0:
        newN = newN * 10 + n % 10
        n = n // 10
    return newN

def sum_digits(n):
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

def product_digits(n):
    mult = 1
    while n != 0:
        digit = n % 10
        mult = mult * digit
        n = n // 10
    return mult

n = input("Enter n : ")
n = int(n)
print(reverse_int(n))
print(sum_digits(n))
print(product_digits(n))

