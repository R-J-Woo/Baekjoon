import sys
input = sys.stdin.readline

n = int(input())
dot = []
for _ in range(n):
    x, y = map(int, input().split())
    dot.append((x, y))

# 정렬 -> 인자 없이 sorted 함수를 이용하면 리스트 아이템의 각 요소 순서대로 정렬한다
# 첫 번째 요소가 같으면 두 번째 요소로 비교한다
sorted_dot = sorted(dot)

for dot in sorted_dot:
    print(dot[0], dot[1])