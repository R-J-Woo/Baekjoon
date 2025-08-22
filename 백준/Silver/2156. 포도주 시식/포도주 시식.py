# 아이디어: 다이나믹 프로그래밍(DP) 알고리즘 이용

import sys
input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 1)
dp[1] = wine[1]

if n > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i-1], # i번째 잔을 마시지 않는 경우
                dp[i-2] + wine[i], # i-1 번째는 건너뛰고, i번째만 마시는 경우
                dp[i-3] + wine[i-1] + wine[i]) # i-1번째와 i번째를 연속해서 마시는 경우 (i-2 번째는 마시면 안됨)
    
print(dp[n])