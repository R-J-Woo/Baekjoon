from itertools import combinations
import bisect
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    B_cards = list(map(int, input().split()))
    A_cards = list(map(int, input().split()))

    B = [sum(c) for c in combinations(B_cards, k)]
    A = [sum(c) for c in combinations(A_cards, k)]
    A.sort()

    min_result = int(1e9)

    # 최솟값은 이분 탐색으로 해결
    for b in B:
        idx = bisect.bisect_left(A, b)

        if idx < len(A):
            min_result = min(min_result, abs(b - A[idx]))
        if idx > 0:
            min_result = min(min_result, abs(b - A[idx - 1]))

    # 최댓값은 max(|minB - maxA|, |maxB - minA|) 이런 식으로 두 가지 경우에서 확인
    max_result = max(
        abs(min(B) - max(A)),
        abs(max(B) - min(A))
    )


    print(min_result, max_result)