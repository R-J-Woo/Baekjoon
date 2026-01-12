N, M = map(int, input().split())
S = list(input())

for i in range(N):
    if S[i] == '0':
        continue

    if M <= 0:
        break

    num = int(S[i])
    count = 10 - num

    if count > M:
        continue
    else:
        M -= count
        S[i] = '0'


S[N - 1] = str((int(S[N - 1]) + M) % 10)

print(''.join(S))