iter, total = map(int, input().split())
iter = int(iter)
total = int(total)

num_list = []

for i in range(iter): # 입력받은 수 만큼 반복하면서 돈을 입력받음
    num = input()
    num_list.append(int(num)) # 입력받은 동전 단위를 리스트에 추가

num_list.sort(reverse=True) # 동전 단위를 내림차순으로 정렬

count = 0

for num in num_list:
    count += total // num
    total %= num

print(count)