B, C, D = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

before = sum(burger) + sum(side) + sum(drink)

burger.sort()
side.sort()
drink.sort()

result = 0
while True:
    if len(burger) == 0 and len(side) == 0 and len(drink) == 0:
        break

    total = 0
    count = 0
    if len(burger) > 0:
        total += burger.pop()
        count += 1
    if len(side) > 0:
        total += side.pop()
        count += 1
    if len(drink) > 0:
        total += drink.pop()
        count += 1

    # 세트로 구매했다면 10% 할인
    if count == 3:
        total = int(total * 0.9)

    result += total

print(before)
print(result)