from collections import deque
import sys
input = sys.stdin.readline

t1 = deque(input().strip())
t2 = deque(input().strip())
t3 = deque(input().strip())
t4 = deque(input().strip())

def rotate(num, dir, visited):
    visited[num] = True
    if num == 1:
        if visited[2] != True and t1[2] != t2[6]:
            if dir == 1:
                rotate(2, -1, visited)
            else:
                rotate(2, 1, visited)
    elif num == 2:
        if visited[1] != True and t2[6] != t1[2]:
            if dir == 1:
                rotate(1, -1, visited)
            else:
                rotate(1, 1, visited)
        if visited[3] != True and t2[2] != t3[6]:
            if dir == 1:
                rotate(3, -1, visited)
            else:
                rotate(3, 1, visited)
    elif num == 3:
        if visited[2] != True and t3[6] != t2[2]:
            if dir == 1:
                rotate(2, -1, visited)
            else:
                rotate(2, 1, visited)
        if visited[4] != True and t3[2] != t4[6]:
            if dir == 1:
                rotate(4, -1, visited)
            else:
                rotate(4, 1, visited)
    elif num == 4:
        if visited[3] != True and t3[2] != t4[6]:
            if dir == 1:
                rotate(3, -1, visited)
            else:
                rotate(3, 1, visited)

    if num == 1:
        t = t1
    elif num == 2:
        t = t2
    elif num == 3:
        t = t3
    elif num == 4:
        t = t4

    if dir == 1: # 시계 방향
        num = t.pop()
        t.appendleft(num)
    else:
        num = t.popleft()
        t.append(num)


k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    visited = [False] * 5
    rotate(num, dir, visited)

sum = 0
if t1[0] == '1':
    sum += 1
if t2[0] == '1':
    sum += 2
if t3[0] == '1':
    sum += 4
if t4[0] == '1':
    sum += 8

print(sum)