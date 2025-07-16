# 아이디어: 주어진 A를 역으로 순회 / 스택 사용
# 현재 수가 스택의 top보다 작다면 현재 스택의 top에 있는 값을 출력
# 현재 수가 스택의 top보다 크다면 스택을 pop
# 위 과정을 반복

n = int(input())
A = list(map(int, input().split()))

stack = []
result = [-1] * n
for i in range(n-1, -1, -1):
    while stack:
        if A[i] < stack[-1]:
            result[i] = stack[-1]
            break
        else:
            stack.pop()

    stack.append(A[i])

print(' '.join(str(num) for num in result))