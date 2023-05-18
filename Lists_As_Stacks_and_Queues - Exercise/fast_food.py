from _collections import deque


def get_order_quantity():
    orders = deque()
    command = input().split()
    for order in command:
        orders.append(int(order))
    return orders


food_for_day = int(input())
orders_queue = get_order_quantity()
print(max(orders_queue))
next_order = orders_queue.copy()
while True:

    if food_for_day <= next_order.popleft():
        print(f"Orders left: {' '.join([str(o) for o in orders_queue])}")
        break
    else:
        food_for_day -= orders_queue.popleft()
        if len(orders_queue) == 0:
            print("Orders complete")
            break

