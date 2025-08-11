import math

n = list(input())
count = [0] * 10
for num in n:
    num = int(num)
    count[num] += 1

count[6], count[9] = math.ceil((count[6] + count[9]) / 2), math.ceil((count[6] + count[9]) / 2)
print(max(count))