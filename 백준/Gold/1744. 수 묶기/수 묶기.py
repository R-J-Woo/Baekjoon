# 아이디어: 양수인 값들과 음수인 값들을 따로 처리
# 양수는 가장 큰 수부터 시작해서 곱한 것과 더한 것을 비교하여 더 큰수를 채택
# 음수 두개를 곱하면 양수로 만들 수 있기 때문에 음수는 가장 작은 수부터 시작해야 함 

import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
for _ in range(n):
    num = int(input())
    if num >= 0:
        plus.append(num)
    else:
        minus.append(num)

# 양수는 오름차순, 음수는 내림차순으로 정렬
plus.sort()
minus.sort(reverse=True)

if len(minus) % 2 != 0 and 0 in plus: # 만약 음수가 홀수개라면 곱해서 양수로 만들 수 없기 때문에 0이 있다면 없앨 수 있음
    plus.remove(0)
    minus.remove(minus[0]) # 가장 큰 음수를 지움 (절댓값이 작은 음수)

total = 0
while len(plus) > 0:
    if len(plus) == 1:
        total += plus[0]
        plus.pop()
    else:
        total += max(plus[-1] + plus[-2], plus[-1] * plus[-2]) # 곱한 것과 더한 것 중 큰 값을 추가
        plus.pop()
        plus.pop()

while len(minus) > 0:
    if len(minus) == 1:
        total += minus[0]
        minus.pop()
    else:
        total += max(minus[-1] + minus[-2], minus[-1] * minus[-2]) # 곱한 것과 더한 것 중 큰 값을 추가
        minus.pop()
        minus.pop()

print(total)