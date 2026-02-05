N, K = map(int, input().split())
L = list(map(int, input().split()))

result = 1
left = 0
bad = 0

for right in range(N - 1):

    if L[right] > K:
        bad += 1

    # bad 1개 이하 유지
    while bad > 1:
        if L[left] > K:
            bad -= 1
        left += 1

    result = max(result, right - left + 2)

print(result)