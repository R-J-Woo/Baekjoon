N = int(input())
A = list(map(int, input().split()))
oper = list(map(int, input().split()))
MAX = -int(1e9)
MIN = int(1e9)


def dfs(result, count, add, minus, multi, div):
    global MAX, MIN
    if count == N:
        MAX = max(result, MAX)
        MIN = min(result, MIN)
        return
    
    if add > 0:
        dfs(result + A[count], count + 1, add - 1, minus, multi, div)
    if minus > 0:
        dfs(result - A[count], count + 1, add, minus - 1, multi, div)
    if multi > 0:
        dfs(result * A[count], count + 1, add, minus, multi - 1, div)
    if div > 0:
        dfs(int(result / A[count]), count + 1, add, minus, multi, div - 1)


dfs(A[0], 1, oper[0], oper[1], oper[2], oper[3])
print(MAX)
print(MIN)