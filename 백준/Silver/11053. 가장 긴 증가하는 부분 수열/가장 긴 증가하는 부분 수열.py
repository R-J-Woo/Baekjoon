n = int(input())
Ai = list(map(int, input().split()))

length = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if Ai[j] < Ai[i]:
            length[i] = max(length[j] + 1, length[i])

print(max(length))