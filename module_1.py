grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# print(sorted(students))
students_sorted = sorted(students)
result = {}
for i in range(len(students_sorted)):
    gr_sum = 0
    for j in range(len(grades[i])):
        gr_sum += grades[i][j]
    gr_avg = gr_sum/len(grades[i])
    new_record = {str(students_sorted[i]): gr_avg}
    # print(new_record)
    result.update(new_record)
print(result)
