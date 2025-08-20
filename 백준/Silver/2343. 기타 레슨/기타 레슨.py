# 아이디어: 이분탐색으로 가능한 블루레이 크기를 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lessons = list(map(int, input().split()))

# 블루레이 최소 크기 = 가장 긴 강의
left = max(lessons)
# 블루레이 최대 크기 = 모든 강의 합
right = sum(lessons)

def count_blurays(size):
    """주어진 블루레이 크기(size)로 몇 개 필요한지 계산"""
    cnt = 1
    total = 0
    for l in lessons:
        if total + l > size:  # 현재 블루레이에 못 넣으면 새 블루레이
            cnt += 1
            total = 0
        total += l
    return cnt

answer = right
while left <= right:
    mid = (left + right) // 2
    if count_blurays(mid) <= m:  # M개 이하로 담을 수 있음 → 크기 줄일 수 있음
        answer = mid
        right = mid - 1
    else:  # M개 초과 → 크기 늘려야 함
        left = mid + 1

print(answer)
