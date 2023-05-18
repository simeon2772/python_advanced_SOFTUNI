def sum_positive(*nums):
    sum_positive_num = 0
    for num in nums:
        if num > 0:
            sum_positive_num += num
    return sum_positive_num


def sum_negative(*nums):
    sum_negative_num = 0
    for num in nums:
        if num < 0:
            sum_negative_num += num
    return sum_negative_num


def print_func(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]

positive_nums = sum_positive(*numbers)
negative_nums = sum_negative(*numbers)

print_func(positive_nums, negative_nums)