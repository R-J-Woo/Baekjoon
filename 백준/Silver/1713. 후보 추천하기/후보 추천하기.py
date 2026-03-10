N = int(input())
R = int(input())
recommend = list(map(int, input().split()))

photos = []  # [학생번호, 추천수, 시간]

for time, student in enumerate(recommend):

    # 이미 사진틀에 있는 경우
    found = False
    for p in photos:
        if p[0] == student:
            p[1] += 1
            found = True
            break

    if found:
        continue

    # 사진틀 남으면 그냥 추가
    if len(photos) < N:
        photos.append([student, 1, time])
        continue

    # 삭제할 학생 찾기
    photos.sort(key=lambda x: (x[1], x[2]))
    photos.pop(0)

    photos.append([student, 1, time])

photos.sort()
for p in photos:
    print(p[0], end = " ")