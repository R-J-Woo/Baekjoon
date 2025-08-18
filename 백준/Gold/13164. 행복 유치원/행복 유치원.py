# 아이디어: 인접한 키 차이를 구하고, 그 중 가장 큰 (K-1)개의 차이를 잘라내면 최소 비용
# 예시
# N=5, K=3, 키: 1 3 5 6 10
# 전체 비용 10 - 1 = 9
# 차이: [2, 2, 1, 4]
# 큰 거 2개 선택: 4, 2 -> 합 6
# 최소 비용 = 9 - 6 = 3

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

# 인접한 차이 계산
diffs = []
for i in range(1, n):
    diffs.append(kids[i] - kids[i-1])

# 큰 차이 (k-1)개 고르기
diffs.sort(reverse=True)

# 전체 비용에서 줄어든 비용 빼기
print(sum(diffs[k-1:]))
