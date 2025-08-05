# 아이디어: 뒷 레벨의 점수부터 역으로 순회
# 현재 레벨의 점수가 뒷 레벨의 점수보다 높다면 뒤 점수보다 1적은 수로 감소

import sys
input = sys.stdin.readline

n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))

result = 0
for i in range(len(score) - 2, -1, -1):
    if score[i] < score[i+1]:
        continue

    result += (score[i] - score[i+1]) + 1
    score[i] = score[i+1] - 1

print(result)