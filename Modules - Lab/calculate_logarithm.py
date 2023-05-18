from math import log


def calculate_lod(num, base):
    if base == 'natural':
        print(f'{log(num):.2f}')
    else:
        base = int(base)
        print(f'{log(num, base):.2f}')


number = int(input())
base = input()
calculate_lod(number, base)
 