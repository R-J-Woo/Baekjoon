import sys
input = sys.stdin.readline

n = int(input())
fluids = list(map(int, input().split()))

# 오름차순 정렬
fluids.sort()

al_idx, san_idx = 0, len(fluids) - 1
al, san = 0, 0
value = float('INF')
while al_idx < san_idx:
    sum = fluids[al_idx] + fluids[san_idx]

    # 특성값이 이전보다 더 0에 가깝다면 갱신
    if abs(sum) < value:
        value = abs(sum)
        al = fluids[al_idx]
        san = fluids[san_idx]

    if sum > 0: # 합이 0보다 크면 산성값을 줄임
        san_idx -= 1
    elif sum < 0: # 합이 0보다 작으면 알칼리 값을 줄임
        al_idx += 1
    else: # 두 값의 합이 0이라면 중지
        break

print(al, san)

# -99, -2, -1
# 98, 4