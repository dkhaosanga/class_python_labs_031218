grade = input('What percentage is your grade?: ')
grade = int(grade)

if grade >= 90:
    if grade > 96:
        print("A+")
    elif grade > 93 and grade <= 96:
        print("A")
    elif grade >= 90:
        print("A-")
elif grade >= 80:
    if grade > 86:
        print("B+")
    elif grade > 83 and grade <= 86:
        print("B")
    elif grade >= 80:
        print("B-")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print(F)

# 50 < n < 100
