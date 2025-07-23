# 아이디어: 각 배열의 모든 부분합을 구해둔다
# 그리고 A의 부분합 X가 있을 때 B의 부분합에 T - X가 되는 경우의 수를 센다

import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# A의 모든 부분합
sumA = {}
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += A[j]
        if temp in sumA:
            sumA[temp] += 1
        else:
            sumA[temp] = 1

# B의 모든 부분합
sumB = {}
for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += B[j]
        if temp in sumB:
            sumB[temp] += 1
        else:
            sumB[temp] = 1

result = 0
for x in sumA:
    if (t - x) in sumB:
        result += (sumA[x] * sumB[t-x]) # 두 개의 수를 곱하면 경우의 수

print(result)