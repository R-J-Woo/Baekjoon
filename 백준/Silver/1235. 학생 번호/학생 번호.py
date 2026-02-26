N = int(input())

students = []
for _ in range(N):
    students.append(input())

# 뒷자리 숫자의 개수 1 ~ 100
for i in range(1, 101):

    result = set()
    for student in students:
        result.add(student[len(student) - i:])

    # 집합의 수와 학생의 수가 같다면
    if len(result) == len(students):
        print(i)
        exit()