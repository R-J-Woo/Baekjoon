from collections import Counter

N = int(input())
A = list(input())
B = list(input())

str_A = []
str_B = []

A_ch = {}
B_ch = {}

for ch in ['a', 'e', 'i', 'o', 'u']:
    A_ch[ch] = 0
    B_ch[ch] = 0

for i in range(N):
    if A[i] in ('a', 'e', 'i', 'o', 'u'):
        A_ch[A[i]] += 1
    else:
        str_A.append(A[i])

    if B[i] in ('a', 'e', 'i', 'o', 'u'):
        B_ch[B[i]] += 1
    else:
        str_B.append(B[i])

flag = True

if ''.join(str_A) != ''.join(str_B):
    flag = False

if A[0] != B[0] or A[-1] != B[-1]:
    flag = False

for ch in ('a', 'e', 'i', 'o', 'u'):
    if A_ch[ch] != B_ch[ch]:
        flag = False

if Counter(A) != Counter(B):
    flag = False

print("YES" if flag else "NO")