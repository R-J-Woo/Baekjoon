# 더 미래의 날짜부터 거꾸로 주식의 가격을 탐색한다.
# 앞에서부터 탐색한다면 미래에 어떤 가격이 있을지 모르기 때문이다.
# 현재의 주식 가격이 현재 기록되어 있는 최대 가격보다 작다면 차익을 실현한다. 
# 그렇지 않다면 현재 최대 가격 기록을 현재의 가격으로 갱신한다.

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    result = 0
    max_price = 0
    for i in range(n - 1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            result += max_price - price[i]
    
    print(result)