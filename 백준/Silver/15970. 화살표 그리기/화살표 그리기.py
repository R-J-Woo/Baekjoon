N = int(input())

color = {}
for _ in range(N):
    x, y = map(int, input().split())

    if y in color:
        color[y].append(x)
    else:
        color[y] = [x]

result = 0
for key in color:
    arr = color[key]
    arr.sort()

    for i in range(len(arr)):
        if i == 0:
            result += abs(arr[i+1] - arr[i])
        elif i == len(arr) - 1:
            result += abs(arr[i] - arr[i-1])
        else:
            value = min(arr[i+1] - arr[i], arr[i] - arr[i-1])
            result += value
    

print(result)