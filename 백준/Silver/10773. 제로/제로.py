

iter = input()

stack = []

for _ in range(int(iter)):
    num = input()
    if int(num) == 0:
        stack.pop()
    else:
        stack.append(int(num))

print(sum(stack))


