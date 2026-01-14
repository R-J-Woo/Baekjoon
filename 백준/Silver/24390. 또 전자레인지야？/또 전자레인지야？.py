M, S = input().split(":")
M = int(M)
S = int(S)
is_cooking = False

result = 0

# M -> 10분 버튼 클릭
if M >= 10:
    result += (M // 10)
    M %= 10

# M -> 1분 버튼 클릭
if M > 0:
    result += M
    M = 0

# S -> 30초 (조리시작) 버튼 클릭
if S >= 30:
    result += (S // 30)
    S %= 30
    is_cooking = True

if S >= 10:
    result += (S // 10)
    S = 0

if not is_cooking:
    result += 1
    is_cooking = True

print(result)