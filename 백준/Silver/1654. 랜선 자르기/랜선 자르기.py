import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lengths = []
for _ in range(K):
    lengths.append(int(input()))

lengths.sort()

start = 1 # zero division error 방지
end = max(lengths)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    # 랜선의 개수 구하기
    for length in lengths:
        if length >= mid:
            total += length // mid

    if total >= N: # 랜선의 개수가 N보다 크면 start를 증가시키고, 최대 길이값 갱신
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)