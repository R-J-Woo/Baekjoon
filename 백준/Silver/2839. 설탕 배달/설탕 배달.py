sugar = input()
sugar = int(sugar)

count = 0

while sugar >= 3:
     
    if sugar % 5 == 0: # 남은 설탕의 무게가 5로 나뉘어지면
        count += sugar // 5
        sugar %= 5
        break

    sugar -= 3
    count += 1


if sugar == 0:
    print(count)
else:
    print(-1)
