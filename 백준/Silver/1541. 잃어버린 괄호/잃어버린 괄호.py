# 아이디어: +를 먼저 처리하고 -를 그 후에 처리하면, +로 커진 수들로 -를 하게 되어서 최솟값이 나올 것이다
import re

S = input()  # 문자열로 입력받음
operator = []
for s in S:
    if s == '+' or s == '-':  # '+', '-'를 나온 순서대로 리스트에 저장
        operator.append(s)
    else:
        continue

operand = re.split("[+-]", S)  # 숫자를 저장하기 위해 '+'와 '-'를 구분
operand = [ele.lstrip('0') for ele in operand]
operand = list(map(int, operand))  # 문자열을 숫자로 변환

while operator:  # operator가 빌 때까지
    if '+' in operator:  # '+'가 있으면
        i = operator.index('+')  # '+'의 위치를 찾기
        num = operand[i] + operand[i+1]  # 더한 값을 다시 저장
        del operand[i:i+2]
        operand.insert(i, num)
        del operator[i]
    else:  # '+'가 더 이상 존재하지 않으면
        break

if '-' in operator:  # '-'가 있으면
    count = 0
    for o in operand:
        count -= o
    count += 2 * operand[0]
else:
    count = operand[0]
print(count)
