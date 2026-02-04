n = int(input())
capsule = {}
for _ in range(n):
    e, n = input().split()
    capsule[e] = n

r = int(input())
for _ in range(r):
    s = list(input().split())
    flag = True
    result = []
    for a in s[1:]:
        if a in capsule:
            result.append(capsule[a])
        else:
            flag = False
            break

    if flag:
        print(' '.join(result))
    else:
        print("YOU DIED")