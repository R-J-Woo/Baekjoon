
# idea: 앞선 회의 종료시간보다 늦게 시작하는 회의 중에서, 회의가 가장 일찍 끝나는 회의로 이어간다

iter = input()

stack = []
command_list = []
for _ in range(int(iter)):
    command = input()
    command_list.append(command)

for command in command_list:
    if command[:4] == "push":
        stack.append(int(command[5:]))
    elif command[:3] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[:4] == "size":
        print(len(stack))
    elif command[:5] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[:3] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

