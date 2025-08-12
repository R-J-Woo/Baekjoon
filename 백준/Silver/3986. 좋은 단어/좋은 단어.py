# 아이디어: 스택을 이용
# 현재 글자가 스택의 top과 같은 글자라면 top에서 삭제, 아니라면 stack에 push
# 좋은 단어라면 stack에 글자가 남아있지 않음

import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())

count = 0
for word in words:
    stack = []
    for w in word:
        if len(stack) > 0 and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)

    if len(stack) == 0:
        count += 1

print(count)