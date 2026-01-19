import math

n = int(input())
A = {}

# 통화 시간(분) 계산
for _ in range(n):
    call, student = input().split()
    hour, minute = map(int, call.split(':'))
    time = hour * 60 + minute
    if student in A:
        A[student] += time
    else:
        A[student] = time

# 통화 요금 계산
total = []
for student, time in A.items():
    if time <= 100:
        money = 10
    else:
        time -= 100
        money = 10 + (3 * math.ceil(time / 50))

    total.append((money, student))

total.sort(key = lambda x: (-x[0], x[1])) # 통화요금 내림차순, 요금이 같으면 학생 이름 오름차순

for t in total:
    print(t[1], t[0])