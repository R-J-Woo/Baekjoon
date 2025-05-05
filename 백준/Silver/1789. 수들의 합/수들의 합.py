s = int(input())

num = 0
total = 0
while True:
    num += 1
    total += num

    if total + (num + 1) > s:
        break

print(num)