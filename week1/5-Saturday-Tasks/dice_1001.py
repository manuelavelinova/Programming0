from random import randint

numberMaria = 1001
numberIvan = 1001

while numberMaria != 0 and numberIvan != 0:
    MariaRolls = 5
    IvanRolls = 5
    while MariaRolls != 0:
        if numberMaria > 0:
            numberMaria -= randint(1,6)
            MariaRolls -= 1
        else:
            numberMaria += randint(1,6)
            MariaRolls -= 1
    print("The current result of Maria is : " + str(numberMaria))
    if numberMaria == 0:
        print("The winner is Maria.")
        break
    while IvanRolls != 0:
        if numberIvan > 0:
            numberIvan -= randint(1,6)
            IvanRolls -= 1
        else:
            numberIvan += randint(1,6)
            IvanRolls -= 1
    print("The current resul of Ivan is : " + str(numberIvan))
    if numberIvan == 0:
        print("The winner is Ivan.")
