N, M, K = map(int, input().split())
seat = [input() for _ in range(N)]

team = '0' * K

count = 0
for i in range(N):
    for j in range(M - K + 1):
        if seat[i][j:j+K] == team:
            count += 1

print(count)