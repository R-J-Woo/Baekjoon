n = int(input())
stone = list(map(int, input().split()))

left = stone[0]
right = stone[1]

for i in range(2, len(stone)):
    if left <= right:
        left += stone[i]
    elif right < left:
        right += stone[i]

diff = abs(left - right)

count = 0
for weight in [100, 50, 20, 10, 5, 2, 1]:
    if diff >= weight:
        count += diff // weight
        diff %= weight

print(count)