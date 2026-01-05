# 그리디 알고리즘
# - 문자열을 앞에서부터 순회하면서 UCPC 글자 순서대로 나오는지 확인

import sys
input = sys.stdin.readline

string = input().strip()
target = "UCPC"
idx = 0

# O(N)
for s in string:
    if idx <= 3 and s == target[idx]:
        idx += 1

if idx > 3:
    print("I love UCPC")
else:
    print("I hate UCPC")