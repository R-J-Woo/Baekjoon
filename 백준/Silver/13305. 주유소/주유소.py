n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

start = 0
end = 1
total_price = 0

while True:
    # end가 끝에 도달했다면 나머지 값 계산 후 종료
    if end == len(length):
        total_price += price[start] * sum(length[start:end])
        break
    # 현재보다 저렴한 주유소를 발견했다면
    elif price[end] < price[start]:
        total_price += price[start] * sum(length[start:end])
        start = end
    else:
        end += 1

print(total_price)