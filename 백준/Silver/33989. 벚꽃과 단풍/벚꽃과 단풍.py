N = int(input())
S = list(input())

D_count = [0] * (N + 1)
B_count = [0] * (N + 1)

for i in range(N):
    if S[i] == 'D':
        D_count[i + 1] = D_count[i] + 1
    else:
        D_count[i + 1] = D_count[i]

for i in range(N - 1, -1, -1):
    if S[i] == 'B':
        B_count[i] = B_count[i + 1] + 1
    else:
        B_count[i] = B_count[i + 1]

result = N
for i in range(0, N + 1):
    result = min(result, D_count[i] + B_count[i])

print(result)