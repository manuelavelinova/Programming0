n = input("Enter n: ")
n = int(n)

start = 6

while True:
     divisor = 1
     sum = 0
     while divisor < start:
         if start % divisor == 0:
             sum += divisor
             
         divisor += 1

     if sum == start:
         print(start)
         n = n - 1
         
     if n == 0:
         break
        
     start += 1
