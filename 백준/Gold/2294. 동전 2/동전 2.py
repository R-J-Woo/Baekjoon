# 아이디어: DP(다이나믹 프로그래밍) 이용
# 동전을 하나씩 확인하면서 해당 금액은 현재까지의 동전 수와 지금의 동전 수를 비교해서 작은 값을 넣음

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [100001] * (k + 1)
dp[0] = 0

for c in coin:
    for i in range(c, k + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])