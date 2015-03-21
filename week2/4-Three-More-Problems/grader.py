min = 0
max = 100

grade = input("Enter the number of points : ")
grade = int(grade)

if grade >= 0 and grade <= 50:
    print("2")
elif grade >= 51 and grade <= 60:
    print("3")
elif grade >= 61 and grade <= 70:
    print("4")
elif grade >= 71 and grade <= 80:
    print("5")
elif grade >= 81 and grade < 100:
    print("6")
elif grade == max:
    print("7")
