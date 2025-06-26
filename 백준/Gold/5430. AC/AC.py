import ast
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    num_list = input().strip()
    num_list = ast.literal_eval(num_list)
    deq = deque(num_list)

    error_flag = False
    reverse_count = 0
    for command in p:
        if command == 'R':
            reverse_count += 1
        elif command == 'D':
            if len(deq) < 1:
                error_flag = True
                break

            if reverse_count % 2 == 0:
                deq.popleft()
            else:
                deq.pop()

    if error_flag == True:
        print('error')
    else:
        if reverse_count % 2 == 0:
            print('[' + ','.join(map(str, deq)) + ']')
        else:
            deq.reverse()
            print('[' + ','.join(map(str, deq)) + ']')