# 아이디어: 최장 증가 부분 수열 (LIS)
# A 전봇대 기준으로 오름차순 정렬
# 그 상태에서 B 전봇대 위치를 보고 최장 증가 부분 수열을 구하면, 최대한 남길 수 있는 전깃줄 수가 됨
# 전체 개수 - LIS 길이 = 제거해야 할 전깃줄 수

import sys
input = sys.stdin.readline

n = int(input())
rope = [tuple(map(int, input().split())) for _ in range(n)]
rope.sort()  # A 전봇대 기준 정렬

# LIS on B 전봇대 위치
dp = [1] * n
for i in range(n):
    for j in range(i):
        if rope[j][1] < rope[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))  # 제거해야 하는 전깃줄 수
