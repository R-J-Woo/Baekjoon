n = int(input())
heights = list(map(int, input().split()))

sequence = [0] * n

seq = 1
for i in range(len(heights)):
    count = 0
    for j in range(len(sequence)):
        if heights[i] == count and sequence[j] == 0:
            sequence[j] = i + 1
            break
        elif sequence[j] == 0:
            count += 1

print(' '.join(str(seq) for seq in sequence))
        