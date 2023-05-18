def read_matrix_func():
    rows, cols = map(int, input().split(', '))
    current_matrix = []
    for row in range(rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)
    return current_matrix


matrix = read_matrix_func()
sum_matrix_elements = sum([sum(col_elements) for col_elements in matrix])

print(sum_matrix_elements)
print(matrix)