n, l = map(int, input().split())
h = list(map(int, input().split()))

h.sort()
for height in h:
    if l >= height:
        l += 1
    else:
        break

print(l)