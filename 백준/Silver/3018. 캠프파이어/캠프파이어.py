N = int(input())
E = int(input())

people = {}
for i in range(1, N + 1):
    people[i] = set()

song_cnt = 0 # 모든 노래의 개수
for _ in range(E):
    numbers = list(map(int, input().split()))
    numbers = numbers[1:]

    # 1이 참가했는지
    flag = False
    if 1 in numbers:
        song_cnt += 1
        flag = True

    # 참가한 사람들이 알고 있는 노래
    total = set()
    for num in numbers:
        total = total | people[num]

    for num in numbers:
        if flag:
            people[num].add(song_cnt)
        else:
            people[num] = total.copy()


for i in range(1, N + 1):
    if len(people[i]) == song_cnt:
        print(i)