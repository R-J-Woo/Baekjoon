N = int(input())
A = list(map(int, input().split()))
Q = int(input())
commands = []
for _ in range(Q):
    commands.append(list(map(int, input().split())))

is_on = [True] * N # 수도꼭지를 켰는지 껐는지 확인
result = sum(A)
print(result)
for c in commands:
    if c[0] == 1:
        i, x = c[1], c[2]
        if is_on[i-1]:
            result -= A[i-1]
            result += x
        A[i-1] = x
    elif c[0] == 2:
        i = c[1]
        if is_on[i-1]:
            is_on[i-1] = False
            result -= A[i-1]
        else:
            is_on[i-1] = True
            result += A[i-1]

    print(result)