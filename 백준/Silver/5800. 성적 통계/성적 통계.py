K = int(input())
score = []
for _ in range(K):
    r = list(map(int, input().split()))
    score.append(r[1:])

for i in range(K):
    largest_gap = 0
    score[i].sort()
    for j in range(1, len(score[i])):
        largest_gap = max(largest_gap, abs(score[i][j] - score[i][j - 1]))

    print("Class", i + 1)
    print("Max " + str(max(score[i])) + ", Min " + str(min(score[i])) + ", Largest gap " + str(largest_gap))