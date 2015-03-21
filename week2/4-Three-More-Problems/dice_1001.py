from random import randint

nMaria = 1001
nIvan = 1001

while nMaria != 0 and nIvan != 0:
    MariaRolls = 5
    IvanRolls = 5
    while MariaRolls != 0:
        if nMaria > 0:
            nMaria -= randint(1,6)
            MariaRolls -= 1
        else:
            nMaria += randint(1,6)
            MariaRolls -= 1
    print("The current result of Maria is : " + str(nMaria))
    if nMaria == 0:
        print("Maria wins")
    while IvanRolls != 0:
        if nIvan > 0:
            nIvan -= randint(1,6)
            IvanRolls -= 1
        else:
            nIvan -= randint(1,6)
            IvanRolls -= 1
    print("The current result of Ivan is : " + str(nIvan))
    if nIvan == 0:
        print("Ivan wins")
