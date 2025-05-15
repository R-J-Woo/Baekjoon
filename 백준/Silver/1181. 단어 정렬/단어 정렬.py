import sys
input = sys.stdin.readline

n = int(input())

alpha = []
for _ in range(n):
    a = input().strip() # 단어 뒤에 \n을 지워줌
    if a not in alpha:
        alpha.append(a)

sorted_alpha = sorted(alpha, key = lambda x : (len(x), x)) # 정렬 조건 1. 단어 길이, 정렬 조건 2. 단어 사전순

for a in sorted_alpha:
    print(a)