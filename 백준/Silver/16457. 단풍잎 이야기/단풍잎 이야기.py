from itertools import combinations

n, m, k = map(int, input().split())
quests = [list(map(int, input().split())) for _ in range(m)]

max_count = 0
for skills in combinations(list(range(1, 2 * n + 1)), n):
    count = 0
    for quest in quests:
        flag = True
        for s in quest:
            if s not in skills:
                flag = False
                break
        if flag:
            count += 1
    max_count = max(max_count, count)

print(max_count)