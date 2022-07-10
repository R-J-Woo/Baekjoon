# 아이디어: 오름차순으로 정렬하여 계산하면 최솟값을 구할 수 있지 않을까
c = int(input())
num_list = list(map(int, input().split()))

l = sorted(num_list)

sum = 0
m = 0  # 누적합
for num in l:
    m += num
    sum += m

print(sum)
