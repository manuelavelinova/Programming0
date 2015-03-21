def calculate_coins(sum):

    coins = {1 : 0,2 : 0,100 : 0,5 : 0,10 : 0,50 : 0,20 : 0}
    sum = round(sum * 100)

    while sum >= 100:
        sum -= 100
        coins[100] += 1
    while sum >= 50:
        sum -= 50
        coins[50] += 1
    while sum >= 20:
        sum -= 20
        coins[20] += 1
    while sum >= 10:
        sum -= 10
        coins[10] += 1
    while sum >= 5:
        sum -= 5
        coins[5] += 1
    while sum >= 2:
        sum -= 2
        coins[2] += 1
    while sum >= 1:
        sum -= 1
        coins[1] += 1

    return coins

result = calculate_coins(2.88)

for key in result:
    value = result[key]
    print(str(key) + " : " + str(value))
