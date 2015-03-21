def square(a):
    return a ** 2

def factoriel(b):
    mult = 1
    while b != 0:
        mult = mult * b
        b = b - 1
    return mult

def count_elements(items):
    counter = 0
    for item in items:
        counter = counter + 1
    return counter

def member(x,xs):
    found = False
    for s in xs:
        if x == s:
            found = True
            break
    return found

def grades_that_pass(students,grades,limit):
    i = 0
    end = len(students) - 1
    result = []
    while i <= end:
        if grades[i] > limit:
            result = result + [students[i]]
            i = i + 1
        i += 1
    return result
