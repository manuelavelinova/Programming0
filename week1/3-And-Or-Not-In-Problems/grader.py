min = 0
max = 100

x = input("Enter the number of points: ")
x = int(x)

if x >=0 and x <= 50:
    print("Grade : 2")
elif x >= 51 and x <= 60:
    print("Grade : 3")
elif x >=61 and x <= 70:
    print("Grade : 4")
elif x >= 71 and x <= 80:
    print("Grade : 5")
elif x >= 81 and x <= 99:
    print("Grade : excellent 6")
elif x == 100:
    print("Grade : verry excellent 7")
