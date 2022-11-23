# CS 303E Quiz 4C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Large Elements
def largeElements(lst):
    large_elements = []
    for x in range(len(lst) - 1):
        if lst[x] >= lst[x+1]:
            large_elements.append(lst[x])
    return large_elements
    pass


# Problem 1: Unequal Midterms
def computeCourseGrade(m1, m2, m3):
    grade = 0
    if m1 > m2 and m1 > m3:
        grade = m1 * .4 + m2 * .3 + m3 * .3
    elif m2 > m1 and m2 > m3:
        grade = m1 * .3 + m2 * .4 + m3 * .3
    else:
        grade = m1 * .3 + m2 * .3 + m3 * .4
    return round(grade)
    pass


def getStudentGrades(lst):
    avg_student = []
    for student in lst:
        avg_student.append([student[0], computeCourseGrade(student[1], student[2], student[3])])
    return avg_student
    pass


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # print(largeElements([6, -1, 28, 27, -6, 29, -1, -21, -20, -28, 13, 15, 2]))
    # print(largeElements([5, 4, 3, 2, 1, 0]))
    # print(largeElements([1, 2, 4, 8, 16, 32]))


    # print(computeCourseGrade(85, 79, 85))
    # print(computeCourseGrade(85, 92, 83))
    # print(getStudentGrades([["Hannah", 85, 79, 85], ["Eli", 85, 92, 83], ["Elena", 96, 95, 100]]))


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT