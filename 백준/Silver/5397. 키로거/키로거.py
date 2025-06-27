# 아이디어: 커서를 기준으로 왼쪽과 오른쪽을 나눠서 두 개의 스택을 사용
# 아렇게 하면 O(1) 시간에 삽입/삭제가 가능

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    command = input().strip()
    
    left = []   # 커서 왼쪽
    right = []  # 커서 오른쪽

    for c in command:
        if c == '<':
            if left:
                right.append(left.pop())
        elif c == '>':
            if right:
                left.append(right.pop())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)

    # 왼쪽 + 오른쪽 뒤집어서 출력
    print(''.join(left + right[::-1]))
