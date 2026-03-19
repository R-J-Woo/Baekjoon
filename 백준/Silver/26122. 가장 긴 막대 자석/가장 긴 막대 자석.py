K = int(input())
M = input()

groups = []
count = 1

# 연속 구간 압축
for i in range(1, K):
    if M[i] == M[i - 1]:
        count += 1
    else:
        groups.append((M[i - 1], count))
        count = 1

groups.append((M[-1], count))

result = 0

# 인접한 N-S 확인
for i in range(len(groups) - 1):
    if groups[i][0] == 'N' and groups[i + 1][0] == 'S':
        result = max(result, 2 * min(groups[i][1], groups[i + 1][1]))

    if groups[i][0] == 'S' and groups[i + 1][0] == 'N':
        result = max(result, 2 * min(groups[i][1], groups[i + 1][1]))

print(result)