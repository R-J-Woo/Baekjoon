n, l = input().split()
n = int(n)
l = int(l)
num_list = list(map(int, input().split()))
num_list = sorted(num_list)  # 오름차순으로 정렬

finish_meter = 0
count = 0
for num in num_list:
    if num > finish_meter:  # 테이프가 붙어있지 않은 자리이면
        count += 1  # 테이프 1개 추가
        finish_meter = num + (l-1)  # 테이프가 붙어있는 거리 갱신
    else:
        continue

print(count)