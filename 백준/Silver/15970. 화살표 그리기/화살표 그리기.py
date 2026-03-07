N = int(input())

black = []
white = []
for _ in range(N):
    x, y = map(int, input().split())

    if y == 1:
        white.append(x)
    else:
        black.append(x)


black.sort()
white.sort()

result = 0
for i in range(len(black)):
    if i == 0:
        result += abs(black[i+1] - black[i])
    elif i == len(black) - 1:
        result += abs(black[i] - black[i-1])
    else:
        value = min(black[i+1] - black[i], black[i] - black[i-1])
        result += value

for i in range(len(white)):
    if i == 0:
        result += abs(white[i+1] - white[i])
    elif i == len(white) - 1:
        result += abs(white[i] - white[i-1])
    else:
        value = min(white[i+1] - white[i], white[i] - white[i-1])
        result += value

print(result)