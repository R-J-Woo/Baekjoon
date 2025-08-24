# 아이디어: 다이나믹 프로그래밍 (DP) 알고리즘 이용

n = int(input())

schedule = []
result = [0] * (n + 1)
for _ in range(n):
    schedule.append(list(map(int, input().split())))

for i in range(len(schedule)):
    t, p = schedule[i]
    if i + t >= len(result):
        continue

    # 이전 현재까지의 최대 이익과, 
    for j in range(i + t, n + 1):
        result[j] = max(result[j], p + result[i])

print(result[n])