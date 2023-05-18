from collections import deque


def add(a, b):
    result = a + b
    return result


def subtraction(a, b):
    result = a - b
    return result


def multiple(a, b):
    result = a * b
    return result


def division(a, b):
    result = a / b
    return result


working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while nectar and working_bees:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()
    if last_nectar < first_bee:
        working_bees.appendleft(first_bee)
        continue
    elif last_nectar >= first_bee:
        operation = symbols.popleft()
        if operation == "+":
            total_honey += abs(add(first_bee, last_nectar))
        if operation == "-":
            total_honey += abs(subtraction(first_bee, last_nectar))
        if operation == "*":
            total_honey += abs(multiple(first_bee, last_nectar))
        if operation == "/":
            total_honey += abs(division(first_bee, last_nectar))

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")