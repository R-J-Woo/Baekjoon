import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    score = []
    for _ in range(n):
        a, b = map(int, input().split())
        score.append((a, b))

    score.sort() # 우선 서류 심사 성적으로 정렬

    test2 = score[0][1]
    count = 1
    for i in range(1, len(score)):
        if score[i][1] < test2: # 면접 순위가 더 훌륭하다면
            test2 = score[i][1]
            count += 1

    print(count)