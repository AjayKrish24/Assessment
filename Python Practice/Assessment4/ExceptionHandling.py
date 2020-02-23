import datetime

class YoungerAge(Exception):
    pass

class Score(Exception):
    pass

print("Registration")
name = input("Enter the name : ")
try:
    dob = input("Enter the DOB (dd-mm-yy) : ")
    day, month, year = dob.split("-")
    datetime.datetime(int(year), int(month), int(day))

    age = int(input("Enter the age : "))
    if age < 15:
        raise YoungerAge("Cannot apply too young")

    mark1 = int(input("Enter the mark1 (1-10) : "))
    mark2 = int(input("Enter the mark2 (1-10) : "))
    mark = mark1 / mark2
    avg = (mark1 + mark2)//2
    if avg < 5:
        raise Score("Too low score to apply")
    print(avg)

# built in exception
except ValueError as e:
    print(e)

except TypeError as e:
    print(e)

except ZeroDivisionError as e:
    print("Mark 2 should not be Zero", e)

# User-defined exception
except YoungerAge as e:
    print(e)

except Score as e:
    print(e)
