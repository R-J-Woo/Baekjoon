# 아이디어: 입력한 숫자들에서 중복을 제거해서 리스트에 넣고 정렬한다 -> ex) [2 4 -10 4 -9] => [-10, -9, 2, 4]
# 그리고 정렬한 리스트에서 입력한 숫자의 인덱스를 찾아서 출력한다

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# 중복 제거하고 정렬
sorted_unique = sorted(set(nums))  # O(NlogN)

# 시간초과를 예방하기 위해 딕셔너리 사용하여 해당 숫자의 인덱스 저장
count_dict = {}
for idx, num in enumerate(sorted_unique):
    count_dict[num] = idx

# 결과 출력
print(' '.join(str(count_dict[num]) for num in nums))