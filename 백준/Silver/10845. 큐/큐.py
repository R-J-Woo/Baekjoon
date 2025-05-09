# 시간 초과(TLE) 가 나는 가장 큰 원인은 input()을 반복문 안에서 너무 많이 호출하기 때문이다
# 백준처럼 많은 입력이 주어지는 경우, 파이썬의 기본 input()은 느리기 때문에 빠른 입력 방법으로 바꿔주는 것이 좋다
# 해결 방법 → sys.stdin.readline() 사용
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
