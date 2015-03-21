first = input("Enter first name : ")
second = input("Enter second name : ")
third = input("Enter third name: ")
year = input("Enter your birth year: ")
year = int(year)

this_year = 2015
currentAge = this_year - year
person = {"first_name " : first, "second_name " : second, "third_name " : third,
          "birth_year " : year, "current_age " : currentAge
          }

print(person)
