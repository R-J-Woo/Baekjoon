N, M = map(int, input().split())

limit = [0] * 101
yj = [0] * 101

now = 1
for _ in range(N):
    length, speed = map(int, input().split())
    
    for _ in range(length):
        limit[now] = speed
        now += 1
    
now = 1
for _ in range(M):
    length, speed = map(int, input().split())
    
    for _ in range(length):
        yj[now] = speed
        now += 1

result = 0
for i in range(len(limit)):
    illegal = yj[i] - limit[i]
    result = max(result, illegal)

print(result)