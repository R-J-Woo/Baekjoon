import sys
input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

nums.sort()
for num in nums:
    print(num)