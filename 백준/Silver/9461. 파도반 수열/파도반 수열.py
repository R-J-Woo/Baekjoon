# 아이디어: n이 4를 넘어가면, 그 이후 삼각형의 변의 길이는 1번째 전 삼각형의 변과
# 5번째 전 삼각형의 변의 길이의 합이다

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n <= 10:
        print(p[n-1])
    else:
        for i in range(10, n):
            p.append(p[i-1] + p[i-5])

        print(p[n-1])