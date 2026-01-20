from collections import deque

a, b = map(int, input().split())
num = ''
queue = deque()
queue.append(num)

result = 0
while queue:
    num = queue.popleft()
    new1 = num + '4'
    new2 = num + '7'

    if int(new1) <= b:
        queue.append(new1)
        if int(new1) >= a:
            result += 1

    if int(new2) <= b:
        queue.append(new2)
        if int(new2) >= a:
            result += 1

print(result)