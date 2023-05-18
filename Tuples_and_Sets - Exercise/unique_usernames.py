n = int(input())

unique_names = set()

for _ in range(n):
    names = input()
    unique_names.add(names)
print(*unique_names, sep='\n')
