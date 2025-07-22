import sys
input = sys.stdin.readline

def binary_search(array, count, start, end):
    max_value = 0
    while start <= end: # log(k)
        total = 0
        mid = (start + end) // 2
        for x in array:
            total += x // mid

        if total >= count:
            start = mid + 1
            max_value = max(max_value, mid)
        else:
            end = mid - 1

    return max_value

n, k = map(int, input().split())
capacity = []
for _ in range(n):
    capacity.append(int(input()))

max_value = binary_search(capacity, k, 1, max(capacity))
print(max_value)