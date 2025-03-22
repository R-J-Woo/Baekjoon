from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    li = sorted(list(map(int, input().split())))
    ans = 0
    dd = defaultdict(int)
    for i in li: 
        dd[i] = 1

    for i in range(n-1):
        for j in range(i+1, n):
            first = li[i]
            second = li[j]
            third = 2*li[j] - li[i]
            if dd[third] == 1: 
                ans += 1
    print(ans)