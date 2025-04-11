def check(mid, scores, k):
    count = 0
    current_sum = 0
    # mid(최소값) 이상인 구간을 K개 넘게 만들 수 있는지 확인
    for score in scores:
        current_sum += score
        if current_sum >= mid:
            count += 1
            current_sum = 0
    return count >= k

def binary_search(n, k, scores):
    left = 0
    right = sum(scores)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        # K개를 넘긴다면 최소값을 증가
        if check(mid, scores, k):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# 입력
n, k = map(int, input().split())
scores = list(map(int, input().split()))

# 출력
print(binary_search(n, k, scores))
