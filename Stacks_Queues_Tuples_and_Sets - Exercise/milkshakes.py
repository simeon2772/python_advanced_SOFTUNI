from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))
milkshakes = 0
while milkshakes != 5 and cups_of_milk and chocolates:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()
    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")

# for choc_el in range(len(chocolates) - 1, -1, -1):
#     for milk_el in range(len(cups_of_milk)):
#         if milkshakes >= 5:
#             print("Great! You made all the chocolate milkshakes needed!")
#             break
#         elif len(chocolates) == 0 or len(cups_of_milk) == 0:
#             print("Not enough milkshakes.")
#             break
#         if chocolates[choc_el] <= 0:
#             chocolates.remove(chocolates[choc_el])
#         elif cups_of_milk[milk_el] <= 0:
#             cups_of_milk.remove(cups_of_milk[milk_el])
#         elif chocolates[choc_el] == cups_of_milk[milk_el]:
#             chocolates.pop()
#             cups_of_milk.popleft()
#             milkshakes += 1
#             continue
#         else:
#             last_cup_of_milk = cups_of_milk.popleft()
#             cups_of_milk.append(last_cup_of_milk)
#             chocolates[choc_el] -= 5
#
# if chocolates:
#     for x in chocolates:
#         print(f"Chocolate: {x}", sep=", ")
# else:
#     print("Chocolate: empty")
# if cups_of_milk:
#     for i in cups_of_milk:
#         print(f"Milk: {i}", sep=", ")
# else:
#     print("Milk: empty")
