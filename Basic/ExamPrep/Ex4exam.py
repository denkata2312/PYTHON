students = int(input())

failing_students = 0
average_students = 0
good_students = 0
excellent_students = 0
average_grade = 0

count = 0

while count < students:
    grade = float(input())

    if 2.00 <= grade <= 2.99:
        failing_students += 1
        average_grade += grade
    elif 3.00 <= grade <= 3.99:
        average_students += 1
        average_grade += grade
    elif 4.00 <= grade <= 4.99:
        good_students += 1
        average_grade += grade
    elif grade >= 5.00:
        excellent_students += 1
        average_grade += grade

    count += 1

print("Top students: {:.2f}%".format(excellent_students / students * 100))
print("Between 4.00 and 4.99: {:.2f}%".format(good_students / students * 100))
print("Between 3.00 and 3.99: {:.2f}%".format(average_students / students * 100))
print("Fail: {:.2f}%".format(failing_students / students * 100))
print("Average: {:.2f}".format(average_grade / students))