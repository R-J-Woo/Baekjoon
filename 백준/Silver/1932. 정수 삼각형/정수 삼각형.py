import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = []
for i in range(1, n + 1):
    dp.append([0] * i)

dp[0][0] = triangle[0][0]
for i in range(n-1):
    for j in range(len(dp[i])):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

print(max(dp[n-1]))