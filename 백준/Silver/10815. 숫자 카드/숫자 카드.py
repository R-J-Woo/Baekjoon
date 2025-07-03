import sys
input = sys.stdin.readline

n = int(input())
cards_num = list(map(int, input().split()))
cards = {}
for card in cards_num:
    if card not in cards:
        cards[card] = 1

m = int(input())
is_has = list(map(int, input().split()))

zero_one = []
for num in is_has:
    if num in cards:
        zero_one.append(1)
    else:
        zero_one.append(0)

print(' '.join([str(num) for num in zero_one]))