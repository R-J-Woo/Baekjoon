# 아이디어: 모든 아이들 중 가장 큰 개수를 원하는 아이를 선택하고, 선물의 개수 중 가장 큰 값이 아이의 수를 만족한다면 1 출력
# 만약, 모든 아이들 중 하나라도 만족하지 못한다면 0 출력

import heapq

n, m = map(int, input().split())
temp_c = list(map(int, input().split()))
w = list(map(int, input().split()))

# 우선순위큐에 넣기 -> 큰 수부터 빼기 위해 -를 붙여서 넣기
c = []
for num in temp_c:
    heapq.heappush(c, -num)

flag = False
for w_num in w:
    c_num = -heapq.heappop(c)

    # 만약 선물 갯수를 만족하면 개수를 빼고 다시 넣기
    if c_num >= w_num:
        c_num -= w_num
        heapq.heappush(c, -c_num)
    else:
        flag = True
        break

if flag == True:
    print(0)
else:
    print(1)