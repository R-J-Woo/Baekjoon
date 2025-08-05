# 아이디어: 그리디 알고리즘 -> 무거운 것부터 처리
# 무게와 박스를 모두 내림차순 정렬
# 해당 crane이 box를 담을 수 있다면 그 box는 boxes 에서 제거

import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()

while len(boxes)>0:
    for crane in cranes:
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    
    time+=1

print(time)