student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_score = sum(student_scores)
# average_score = total_score / len(student_scores)
# print(total_score)
# print(average_score)
sum = 0
max = student_scores[0]
min = student_scores[0]
for score in student_scores:
    if max <= score:
        max = score
    if min >= score:
        min = score
#     sum += score
# print(sum)
print(f"Max Score: {max}\nMin Score: {min}")
