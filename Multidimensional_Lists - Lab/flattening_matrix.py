matrix = [[int(el) for el in input().split(', ')] for row in range(int(input()))]
flattered_matrix = [num for row in matrix for num in row]
print(flattered_matrix)
