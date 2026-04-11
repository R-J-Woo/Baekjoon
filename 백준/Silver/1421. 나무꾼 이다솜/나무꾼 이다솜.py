import sys
input = sys.stdin.readline

N, C, W = map(int, input().split())
trees = [int(input()) for _ in range(N)]

result = 0

# 가능한 길이 L 탐색
for L in range(1, max(trees) + 1):
    total = 0

    for tree in trees:
        pieces = tree // L
        if pieces == 0:
            continue

        # 자르는 횟수 계산
        if tree % L == 0:
            cuts = pieces - 1
        else:
            cuts = pieces

        profit = pieces * L * W - cuts * C

        if profit > 0:
            total += profit

    result = max(result, total)

print(result)