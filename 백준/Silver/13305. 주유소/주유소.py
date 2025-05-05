n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

start = 0
total_price = 0
while True:
    # 이후의 주유소 중에 현재 주요소보다 저렴한 곳이 없다면
    if not any(p < price[start] for p in price[start:len(price)-1]):
        total_price += price[start] * sum(length[start:])
        break
    
    # 현재 주유소보다 저렴한 곳이 있다면
    length_now = 0
    for i in range(start, len(price)):
        # 현재 주유소 보다 가격이 저렴한 주유소를 발견한다면
        if price[start] > price[i]: 
            length_now = sum(length[start:i])
            total_price += length_now * price[start] # 가격 업데이트
            start = i # 시작점 업데이트
            break

print(total_price)