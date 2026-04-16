N = int(input())

war = {}
collect = list(input().split())
for i in range(N):
    war[collect[i]] = i + 1

hw = list(input().split())
total = 0
result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        total += 1
        if war[hw[i]] < war[hw[j]]:
            result += 1


print(str(result) + '/' + str(total))