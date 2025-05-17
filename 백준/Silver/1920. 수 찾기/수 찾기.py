import sys
input = sys.stdin.readline

def binary_search(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        # 중간 값이 찾는 숫자보다 크다면 right 감소
        if array[mid] > target:
            right = mid - 1
        # 중간 값이 찾는 숫자보다 작다면 left 증가
        elif array[mid] < target:
            left = mid + 1
        # 중간 값과 찾는 숫자가 같다면 탐색 중지
        else:
            return mid
        
    return None


n = int(input())
A = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

A.sort()
for num in nums:
    result = binary_search(A, num, 0, len(A) - 1)
    if result != None:
        print(1)
    else:
        print(0)