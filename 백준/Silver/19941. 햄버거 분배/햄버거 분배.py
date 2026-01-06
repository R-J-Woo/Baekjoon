# 그리디 알고리즘
# - 각 사람이 자신이 먹을 수 있는 햄버거 중 가장 앞에 있는 햄버거를 먹음

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
hp_list = list(input().strip())

count = 0
for i in range(len(hp_list)):
    # 사람이 있을 때
    if hp_list[i] == 'P':
        # 가능한 거리 중 가장 앞의 햄버거를 먹음
        for j in range(max(0, i - K), min(i + K + 1, len(hp_list))):
            if hp_list[j] == 'H':
                count += 1
                hp_list[j] = 'E'
                break

print(count)