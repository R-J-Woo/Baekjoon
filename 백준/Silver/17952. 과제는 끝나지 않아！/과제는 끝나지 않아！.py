import sys
input = sys.stdin.readline

N = int(input())

homework = []
result = 0

for _ in range(N):
    work = list(map(int, input().split()))
    if work[0] != 0:
        homework.append([work[1], work[2]])

    # 할 과제가 없으면 패스
    if len(homework) == 0:
        continue

    now = homework.pop()
    now[1] -= 1
    if now[1] == 0:
        result += now[0]
    else:
        homework.append(now)

print(result)