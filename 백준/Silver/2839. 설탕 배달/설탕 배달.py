kg = int(input())

count = 0
while kg >= 0:
    # 5로 나눠지는 순간 바로 종료
    if kg % 5 == 0:
        count += kg // 5
        print(count)
        break
    else:
        count += 1
        kg -= 3

else:
    print(-1)