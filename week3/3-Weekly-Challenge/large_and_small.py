def to_digits_min(n):  
    digits = []

    while n != 0:
        digit = n % 10
        digits += [digit]
        n = n // 10

    sortDigits = sorted(digits)

    minNumber = 0

    for digit in sortDigits:
        minNumber = minNumber * 10 + digit

    return minNumber


def max_number(n):
    maxNumber = 0
    maxDigits = []
    minNumber = to_digits_min(n)
    while minNumber != 0:
        maxDigit = minNumber % 10
        maxDigits += [maxDigit]
        minNumber = minNumber // 10

    for maxDigit in maxDigits:
        maxNumber = maxNumber * 10 + maxDigit

    return maxNumber
        
