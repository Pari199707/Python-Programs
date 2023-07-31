def marksToGrades(x):
    if x>90:
        return 'A'
    elif x>80:
        return 'B'
    elif x>70:
        return 'C'
    elif x>60:
        return 'D'
    elif x>50:
        return 'E'
    else:
        return 'F'

marks=[98,67,56,78,45,34]
sorted_marks=sorted(marks)
grades=list(map(marksToGrades,marks))
print(grades)
sorted_grades=list(map(marksToGrades,sorted_marks))
print(sorted_grades)

