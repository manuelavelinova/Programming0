def is_prime(n):
    start = 2
    is_prime = True
    
    if n == 0:
        is_prime = False
        
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        else:
            start += 1
            
    return is_prime
            
def prime_pair(numbers):
    for i in range(0,len(numbers) - 1):
        for j in range(i,len(numbers)):
            if is_prime(numbers[i] + numbers[j]):
                return True
            else:
                return False

print(prime_pair([4,6,8]))
