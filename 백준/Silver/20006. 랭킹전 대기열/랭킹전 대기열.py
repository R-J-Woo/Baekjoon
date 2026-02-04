p, m = map(int, input().split())

rooms = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    
    if len(rooms) == 0:
        rooms.append([(n, l)])
        continue

    flag = False
    for room in rooms:
        if abs(l - room[0][1]) <= 10 and len(room) < m:
            room.append((n, l))
            flag = True
            break

    # 기존에 있던 방에 넣지 못했다면
    if not flag:
        rooms.append([(n, l)])


for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort()
    for name, level in room:
        print(level, name)