def is_prime(n):
    start = 2
    isPrime = True
    if n == 1:
            isPrime = False
    while start < n:
        if n % start == 0:
            isPrime = False
            break
        
        start += 1

    return isPrime

p = input("Enter p :")
p = int(p)

q = p - 2
r = p + 2
is_p_prime = is_prime(p)
is_q_prime = is_prime(q)
is_r_prime = is_prime(r)

if is_p_prime and (not is_q_prime) and (not is_r_prime):
    print(str(p) + " is prime")
    print("But " + str(q) + " and " + str(r) + " are not.")
elif is_p_prime:
    if is_q_prime:
        print(q, p)
    if is_r_prime:
        print(p, r)
else:
    print(str(p) + " is not prime.")
