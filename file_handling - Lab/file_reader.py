def read_file_and_sum_numbers(file_name):
    data = open(file_name, 'r')
    sum_numbers = 0

    for num in data:
        sum_numbers += int(num)

    return sum_numbers


result = read_file_and_sum_numbers('numbers.txt')
print(result)
 