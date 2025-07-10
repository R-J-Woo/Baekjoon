# 아이디어: 패키지와 낱개 가격의 최저가 구하고, 패키지만 구매 / 낱개만 구매 / 혼합해서 구매하는 방법 중 가장 저렴한 가격 구하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 패키지와 낱개 가격의 최저가 구하기
package, piece = int(1e9), int(1e9)
for _ in range(m):
    x, y = map(int, input().split())
    if x < package:
        package = x
    if y < piece:
        piece = y

# 패키지만 구매, 낱개만 구매, 혼합해서 구매하는 방법 중 가장 저렴한 가격 구하기
value1 = package * ((n // 6) + 1)
value2 = package * (n // 6) + piece * (n % 6)
value3 = piece * n

min_value = min(value1, value2)
min_value = min(min_value, value3)

print(min_value)