N = int(input())
A = list(input())
B = list(input())

str_A = []
str_B = []

noun_A, noun_B = {}, {}
for code in range(ord('a'), ord('z') + 1):
    ch = chr(code)
    noun_A[ch] = 0
    noun_B[ch] = 0

for i in range(N):
    if A[i] not in ('a', 'e', 'i', 'o', 'u'):
        str_A.append(A[i])

    if B[i] not in ('a', 'e', 'i', 'o', 'u'):
        str_B.append(B[i])

    noun_A[A[i]] += 1
    noun_B[B[i]] += 1

flag = True

# 모음을 제거한 문자열 동일
if ''.join(str_A) != ''.join(str_B):
    flag = False

# 첫 글자와 마지막 글자가 동일
if A[0] != B[0] or A[-1] != B[-1]:
    flag = False

# 한 단어를 재배열해 다른 단어를 생성 가능
if noun_A != noun_B:
    flag = False

print("YES" if flag else "NO")