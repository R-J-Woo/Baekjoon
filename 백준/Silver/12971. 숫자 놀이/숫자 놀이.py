l = list(map(int, input().split()))
p, x = l[:3], l[3:]

max_p = max(p)
max_idx = p.index(max_p)
n = x[max_idx]
while True:
    if n >= 300 * 300 * 300:
        print(-1)
        break

    flag = True
    for j in range(3):
        if (n % p[j]) != x[j]:
            flag = False
            break

    if flag:
        print(n)
        break

    n += max_p