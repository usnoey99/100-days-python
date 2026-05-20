# Create a new list from numbers, where you added 1 to each value
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]

name = "Felipe"
letter_list = [letter for letter in name]

double_list = [num * 2 for num in range(1,5)]
print(double_list) # [2, 4, 6, 8]

names = ["Alex", "Beth", "Carolin", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names) # ['Alex', 'Beth', 'Dave']

upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names) # ['CAROLIN', 'ELANOR', 'FREDDIE']

import random
student_score = {student:random.randint(50, 100) for student in names}
print(student_score)

passed_students = {student: score for (student, score) in student_score.items() if score >= 80}
print(passed_students)