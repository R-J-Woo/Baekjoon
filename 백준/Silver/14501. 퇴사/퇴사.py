# 아이디어: 다이나믹 프로그래밍 (DP) 알고리즘 이용

n = int(input())

schedule = []
result = [0] * (n + 1)
for _ in range(n):
    schedule.append(list(map(int, input().split())))

for i in range(len(schedule)):
    t, p = schedule[i]
    # 상담을 할 수 없다면 패스
    if i + t >= len(result):
        continue

    # i번째 날까지 고려했을 때 얻을 수 있는 최대 이익 비교 후 갱신
    for j in range(i + t, n + 1):
        result[j] = max(result[j], p + result[i]) # 이전까지의 최대 이익 방식과 현재 비교

print(result[n])