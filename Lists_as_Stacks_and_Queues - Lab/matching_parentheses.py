data = input()

stack = []

for i in range(len(data)):
    ch = i

    if data[ch] == "(":
        stack.append(ch)
    elif data[ch] == ")":
        start_index = stack.pop()
        print(data[start_index:ch + 1])

