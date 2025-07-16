n = int(input())
A = input()

stack = []
valid = [0] * n  # 각 인덱스가 유효한 괄호쌍이면 1로 표시

for i in range(n):
    if A[i] == ')' and stack:
        if A[stack[-1]] == '(':
            valid[i] = 1
            valid[stack[-1]] = 1
            stack.pop()
        else:
            stack.append(i)
    else:
        stack.append(i)

# 이제 유효한 구간의 연속 최대 길이를 찾자
max_len = cnt = 0
for i in range(n):
    if valid[i]:
        cnt += 1
        max_len = max(max_len, cnt)
    else:
        cnt = 0

print(max_len)