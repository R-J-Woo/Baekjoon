import sys
input = sys.stdin.readline

N, M = map(int, input().split())

students = {}
for i in range(1, N + 1):
    students[i] = []

while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break

    a = int(a)
    if len(students[a]) < M:
        students[a].append(b)

# 길이가 짧은 순, 사전 순으로 정렬
for i in range(1, N + 1):
    students[i].sort(key = lambda x: (len(x), x))

# 청팀(홀수) 출력
for i in range(1, N + 1):
    if i % 2 == 1:
        for student in students[i]:
            print(i, student)

# 백팀(짝수) 출력
for i in range(1, N + 1):
    if i % 2 == 0:
        for student in students[i]:
            print(i, student)