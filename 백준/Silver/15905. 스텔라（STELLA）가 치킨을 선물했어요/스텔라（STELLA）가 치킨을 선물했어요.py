N = int(input())

score = []
for _ in range(N):
    a, b = map(int, input().split())
    score.append((a, -b))

score.sort(reverse=True)

result = 0
if len(score) > 5:
    for i in range(5, len(score)):
        if score[i][0] == score[4][0]:
            result += 1

print(result)