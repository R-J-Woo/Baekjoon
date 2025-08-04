import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A, B = [], []
for _ in range(n):
    A.append(list(input().strip()))

for _ in range(n):
    B.append(list(input().strip()))

result = 0
for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]:
            result += 1
            for a in range(3):
                for b in range(3):
                    if A[i+a][j+b] == '1':
                        A[i+a][j+b] = '0'
                    else:
                        A[i+a][j+b] = '1'

if A != B:
    print(-1)
else:
    print(result)