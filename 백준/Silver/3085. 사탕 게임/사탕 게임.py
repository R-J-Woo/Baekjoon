import sys
input = sys.stdin.readline

n = int(input())
maps = []
for _ in range(n):
    row = input().strip()
    maps.append([i for i in row])

def get_count(maps): # O(N^2)
    max_count = 0
    # 행
    for i in range(len(maps)):
        count = 1
        for j in range(1, len(maps[0])):
            if maps[i][j] == maps[i][j-1]: # 이전 칸과 동일한 색상이라면
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    # 열
    for j in range(len(maps[0])):
        count = 1
        for i in range(1, len(maps)):
            if maps[i][j] == maps[i-1][j]: # 이전 칸과 동일한 색상이라면
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    return max_count


max_count = 0
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if i + 1 < n: # 아래칸과 교환
            maps[i][j], maps[i+1][j] = maps[i+1][j], maps[i][j]
            count = get_count(maps)
            max_count = max(count, max_count)
            maps[i][j], maps[i+1][j] = maps[i+1][j], maps[i][j]
        if j + 1 < n: # 오른쪽칸과 교환
            maps[i][j], maps[i][j+1] = maps[i][j+1], maps[i][j]
            count = get_count(maps)
            max_count = max(count, max_count)
            maps[i][j], maps[i][j+1] = maps[i][j+1], maps[i][j]

print(max_count)