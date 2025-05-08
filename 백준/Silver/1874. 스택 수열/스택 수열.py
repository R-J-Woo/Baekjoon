n = int(input())

# 수열 담기
seq = []
for _ in range(n):
    s = int(input())
    seq.append(s)

stack = []
operations = []
for i in range(1, n + 1):
    if i <= seq[0]: # 아직 스택에 담겨있지 않은 숫자라면
        operations.append("+")
        stack.append(i)
    
    while len(stack) > 0 and stack[-1] == seq[0]:
        operations.append("-")
        seq.pop(0)
        stack.pop()

if len(stack) > 0:
    print("NO")
else:
    for op in operations:
        print(op)