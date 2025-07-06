import sys
input = sys.stdin.readline

n = int(input())
expression = input().strip()
values = [int(input()) for _ in range(n)]

stack = []

for ch in expression:
    if ch.isalpha():  # 알파벳인 경우
        index = ord(ch) - ord('A')
        stack.append(values[index])
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)  # 실수 나눗셈

# 소수 둘째 자리까지 출력
print(f"{stack[0]:.2f}")