grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
print(type(students))
list.sort(students)
print(students)

# print(sum(grades[0]) / len(grades[0]))

averages = []
for grade_list in grades:
    average = sum(grade_list) / len(grade_list)
    averages.append(average)

print(averages)

program = dict(zip(students, averages))
print(program)





