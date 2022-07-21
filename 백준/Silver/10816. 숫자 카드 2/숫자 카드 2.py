from bisect import bisect_left, bisect_right

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
ints = list(map(int, input().split()))

cards.sort()

for i in ints:
    li = bisect_left(cards, i)
    ri = bisect_right(cards, i)
    print(ri-li, end=" ")
