# 아이디어: 이분탐색으로 적절한 횟수를 탐색

n, m = map(int, input().split())
price = []
for _ in range(n):
    price.append(int(input()))

start = max(price)
end = sum(price)
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1 # 인출 횟수
    balance = mid

    for money in price:
        if balance < money: # 현재 잔고가 부족하다면 인출 1회 추가
            balance = mid
            count += 1

        balance -= money # 금액 차감

    if count <= m: # 인출 횟수가 m보다 작다면 갱신
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)