# 아이디어: 마이너스가 나와도 손해가 되지 않기 때문에 팁이 큰 순서대로 받고, 팁이 작은 사람은 뒷 순위로 뺌

import sys
input = sys.stdin.readline

N = int(input())
tips = []
for _ in range(N):
    tips.append(int(input()))

tips.sort(reverse=True)

result = 0
for i in range(len(tips)):
    result += max(0, (tips[i] - i))

print(result)