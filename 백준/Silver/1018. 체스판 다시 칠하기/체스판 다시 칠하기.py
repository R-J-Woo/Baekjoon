import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = []
for _ in range(n):
    row = input().strip()
    map.append([i for i in row])

def get_count(map, x, y, start): # O(64)
    count = 0
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if ((i - x) + (j - y)) % 2 == 0 and map[i][j] != start: # 움직인 칸이 짝수인데 동일한 색상이 아니라면
                count += 1
            elif ((i - x) + (j - y)) % 2 != 0 and map[i][j] == start: # 움직인 칸이 홀수인데 동일한 색상이면
                count += 1

    return count

min_count = int(1e9)
for i in range(n - 7):
    for j in range(m - 7):
        count = min(get_count(map, i, j, 'B'), get_count(map, i, j, 'W'))
        min_count = min(min_count, count)

print(min_count)
