import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
m = int(input())
for _ in range(m):
    command = list(input().split())
    if command[0] == 'L' and len(left) > 0:
        w = left.pop()
        right.append(w)
    elif command[0] == 'D' and len(right) > 0:
        w = right.pop()
        left.append(w)
    elif command[0] == 'B' and len(left) > 0:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print(''.join(left) + ''.join(reversed(right)))