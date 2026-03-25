# 왼쪽에 자기보다 큰 사람이 있는 만큼 빈 자리를 두고 자리를 들어간다
# ex) 0을 빈자리라고 할 때, [0, 1, 0, 0, 0]에서 왼쪽에 큰 사람이 2명이라면
# [0, 1, 0, 2, 0] 이런식으로 한다
# 키가 작은 사람부터 시작하므로 왼쪽 빈 자리에는 자기보다 큰 사람이 들어갈 수 밖에 없다

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
        