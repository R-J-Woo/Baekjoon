from itertools import combinations_with_replacement

count = int(input())

nums = [1, 5, 10, 50]
num_list = []
for com in combinations_with_replacement(nums, count):
    total_num = sum(com)
    if total_num not in num_list:
        num_list.append(total_num)

print(len(num_list))