# 아이디어: 그리디 알고리즘
# 현재 앞의 4개의 칸에 .이 없고 AAAA로 만들 수 있으면 만들고,
# 그 다음 BB로 만들 수 있으면 BB로 만들고
# .이면 건너뛴다

board = list(input().split('.'))
result = []
flag = False

for b in board:
    if len(b) % 2 != 0:
        flag = True
        break

    a = len(b) // 4
    b = (len(b) % 4) // 2
    result.append('AAAA' * a + 'BB' * b)

if flag == True:
    print(-1)
else:
    print('.'.join(result))