# 입력을 input()으로 받기보다는 sys.stdin.readline으로 받는 것이 더 빠르다
from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop" or command[0] == "front" or command[0] == "back":
        if len(queue) == 0:
            print(-1)
        elif command[0] == "pop":
            print(queue.popleft())
        elif command[0] == "front":
            print(queue[0])
        elif command[0] == "back":
            print(queue[-1])
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)