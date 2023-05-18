number_of_operations = int(input())
students_dict = {}
for _ in range(number_of_operations):
    students_name, students_grade = input().split()

    if students_name not in students_dict:
        students_dict[students_name] = []
    students_dict[students_name].append(float(students_grade))

for student, grade in students_dict.items():
    convert_to_string = " ".join(map(lambda g: f"{g:.2f}", grade))
    average_grade = sum(grade) / len(grade)
    print(f'{student} -> {convert_to_string} (avg: {average_grade:.2f})')
