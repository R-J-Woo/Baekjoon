# 아이디어: DP 알고리즘 이용
# dp[i][j] -> 길이가 i이고, 마지막 숫자가 j인 계단 수의 개수
# 마지막 자리가 j라면, 그 전 자리는 j-1 또는 j+1이어야 함

n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

# 길이가 1일 때 초기화
for j in range(1, 10):
    dp[1][j] = 1

# 점화식
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        dp[i][j] %= 1000000000

print(sum(dp[n]) % 1000000000)
