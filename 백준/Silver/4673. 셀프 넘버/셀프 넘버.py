# 아이디어: 숫자를 1부터 하나씩 커지는 방식으로 돌면서 생성될 수 있는 수를 구함
# 예) 1 -> 2, 2 -> 4, ... 10 -> 11, 11 --> 13 등으로
# 마지막까지 돌았을 때 생성되지 않은 수가 셀프 넘버

def get_selfNum(num):
    num_list = list(str(num))
    sum = 0
    for n in num_list:
        sum += int(n)
    sum += num
    return sum

max_selfNum = 1
self_nums = set()

for i in range(1, 10001):
    self_num = get_selfNum(i)
    self_nums.add(self_num)

for i in range(1, 10001):
    if i not in self_nums:
        print(i)