import sys
input = sys.stdin.readline

n = int(input())
spots = []
for _ in range(n):
    x, y = map(int, input().split())
    spots.append((y, x)) # y, x 순으로 넣어서, 정렬 시 첫 번째로 y 그 후 x로 정렬되게 함

spots.sort()
for spot in spots:
    print(spot[1], spot[0])