n = int(input())
cheese = list(input().split())

result = set()

for c in cheese:
    if len(c) >= 6 and c[-6:] == 'Cheese':
        result.add(c)

if len(result) >= 4:
    print("yummy")
else:
    print("sad")