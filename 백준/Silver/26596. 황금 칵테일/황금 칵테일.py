import sys
input = sys.stdin.readline

M = int(input())

ingredient = {}
for _ in range(M):
    s, x = input().split()
    if s in ingredient:
        ingredient[s] += int(x)
    else:
        ingredient[s] = int(x)

l = []
for key, value in ingredient.items():
    l.append([value, key])

l.sort()
is_delicious = False
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if int(float(l[i][0]) * 1.618) == l[j][0]:
            is_delicious = True

if is_delicious:
    print("Delicious!")
else:
    print("Not Delicious...")