import sys
input = sys.stdin.readline

s = input()
count_zero, count_one = 0, 0
last_num = '-1'
for i in range(len(s)):
    if s[i] != last_num: # 0에서 1로 변하거나, 1에서 0으로 변하면
        if s[i] == '1':
            count_one += 1
            last_num = '1'
        elif s[i] == '0':
            count_zero += 1
            last_num = '0'

print(min(count_zero, count_one))