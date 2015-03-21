n = input("Enter three numbered number  n : ")
n = int(n)

first = n // 100
second = (n // 10) % 10
third = n % 10

if first >= second and first >= third and second >= third:
    print("Max is : " + str(first) + str(second) + str(third))
    print("Min is :  " + str(third + second  + third))
    
elif first >= second and first >= third and second <= third:
    print("Max is : " + str(first) + str(third) + str(second))
    print("Min is  : " + str(second) + str(third) + str(first))
          
elif second >= first and second >= third and first >= third:
    print("Max is " + str(second) + str(first) + str(third))
    print("Min is : " + str(third) + str(first) + str(second))
          
elif second >= first and second  >= third and first <= third:
    print("Max is : " + str(second) + str(third) + str(first))
    print("Min is : " + str(first + third  + second))
          
elif third >= first and third >= second and first >= second:
    print("Max is : " + str(third) + str(first) + str(second))
    print("Min is : " + str(second) + str(first) + str(third))
          
elif third >= first and third >= second and first <= second:
    print("Max is : " + str(third) + str(second) + str(first))
    print("Min is : " + str(first) + str(second) + str(third))  
