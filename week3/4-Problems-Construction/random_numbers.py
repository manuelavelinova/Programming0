from random import randint
def generate_random_list(n,start,end):
    list = []
    while n != 0:
        integer = randint(start,end)
        list += [integer]
        n = n - 1
        
    return list


