# 아이디어: 두 문자열을 반복하여 길이를 맞춘 후에 두 문자열이 같으면 1, 아니면 0

s = input()
t = input()

if s * len(t) == t * len(s):
    print(1)
else:
    print(0)