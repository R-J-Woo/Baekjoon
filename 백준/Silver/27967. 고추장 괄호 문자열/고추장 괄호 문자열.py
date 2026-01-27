N = int(input())
brackets = list(input())

# 우선 주어진 문자열에서 괄호의 개수를 세기
left = 0
right = 0
for b in brackets:
    if b == '(':
        left += 1
    elif b == ')':
        right += 1

# ) 형태의 괄호가 ( 괄호보다 먼저 나오면 잘못된 문자열
# ( 괄호의 개수가 N의 절반이 될 때까지 G를 ( 로 먼저 바꿔주기
for i in range(len(brackets)):
    if brackets[i] == 'G':
        if left < (N // 2):
            brackets[i] = '('
            left += 1
        else:
            brackets[i] = ')'
            right += 1

print(''.join(brackets))