n = int(input())
fluids = list(map(int, input().split()))

Aidx = 0
Sidx = len(fluids) - 1
result = float('INF')
a, s = 0, 0
while Aidx < Sidx:
    sum = fluids[Aidx] + fluids[Sidx]
    if abs(sum) < abs(result): # 현재 용액의 합이 이전보다 0에 더 가까우면
        result = sum
        a, s = fluids[Aidx], fluids[Sidx]

    if sum > 0:
        Sidx -= 1
    elif sum < 0:
        Aidx += 1
    else: # 합이 0이면 종료
        break

print(a, s)