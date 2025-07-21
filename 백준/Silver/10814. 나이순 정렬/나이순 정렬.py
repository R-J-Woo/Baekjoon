# 아이디어: 나이 / 이름에 추가로 입력된 순서를 함께 저장
# 나이 순으로 정렬하고, 나이가 같으면 입력된 순서로 정렬되도록 함

import sys
input = sys.stdin.readline

n = int(input())
customer = []
for i in range(n):
    age, name = input().split()
    customer.append((int(age), i, name))

customer.sort()
for c in customer:
    print(c[0], c[2])