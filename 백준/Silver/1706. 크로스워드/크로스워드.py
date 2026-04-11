R, C = map(int, input().split())
graph = [input() for _ in range(R)]

words = []
for i in range(R):
    temp = graph[i].split('#')
    for word in temp:
        if len(word) >= 2:
            words.append(word)

for j in range(C):
    temp = ""
    for i in range(R):
        if graph[i][j] == '#':
            if len(temp) >= 2:
                words.append(temp)
            temp = ""
        else:
            temp += graph[i][j]

    # 마지막 처리
    if len(temp) >= 2:
        words.append(temp)


print(min(words))