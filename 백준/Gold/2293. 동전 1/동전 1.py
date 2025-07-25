# 아이디어: 다이나믹 프로그래밍 이용

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = []
for _ in range(n):
    values.append(int(input()))

total_list = [0] * (k + 1)
# 화폐 단위를 순회
for i in range(len(values)):
    for j in range(values[i], k + 1):
        if j == values[i]:
            total_list[j] += 1
        # 해당 가치의 합만큼 될 수 있다면 될 수 있는 경우의 수만큼 더해줌
        elif total_list[j - values[i]] != 0:
            total_list[j] += total_list[j - values[i]]


print(total_list[-1])
