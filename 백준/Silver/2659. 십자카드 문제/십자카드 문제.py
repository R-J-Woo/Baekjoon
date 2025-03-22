# 시계수 찾기
def get_clock_num(num_list):
    rotations = []
    for i in range(len(num_list)):
        num = int(''.join(map(str, num_list[i:] + num_list[:i])))
        rotations.append(num)
    return min(rotations)

# 모든 시계수 조합
clock_numbers = []
for i in range(1111, 10000):
    if '0' not in str(i):
        num_list = list(map(int, str(i)))
        clock_num = get_clock_num(num_list)
        if clock_num not in clock_numbers:
            clock_numbers.append(clock_num)

clock_numbers.sort()

nums = list(map(int, input().split()))
clock_num = get_clock_num(nums)

print(clock_numbers.index(clock_num) + 1)