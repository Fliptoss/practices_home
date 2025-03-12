#python dictornaries
programming_dictonary = {"bug": "This is a bug",
                         "bug2": "this is another bug",
                         "bug3": "this is another bug", }

for key in programming_dictonary:
    print(programming_dictonary[key])

'''
tast 1
'''
student_score = {
    "s1": 81,
    "s2": 77,
    "s3": 92,
    "s4": 66,
    "s5": 45
}

student_grades = {}

for key in student_score:
    score = student_score[key]
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Well done"
    elif score > 70:
        student_grades[key] = "Acceptable"
    elif score > 60:
        student_grades[key] = "Try to do better"
    else:
        student_grades[key] = "Fail"

print(student_grades)

