# 아이디어: 우선 2원으로 거스름돈을 빼다가 5의 배수가 나오면 5로 나누기
# ex) 14 -> 12 -> 10 -> 5 -> 0
# 거스름돈을 빼다가 0보다 크지만 2보다 작은 수가 나오면 거슬러 줄 수 없으므로 -1

n = int(input())

count = 0
while n >= 2:
    if n % 5 != 0:
        n -= 2
        count += 1
    else:
        count += n // 5
        break

if n > 0 and n < 2:
    print(-1)
else:
    print(count)