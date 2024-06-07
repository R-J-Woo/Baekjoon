
# idea: 앞선 회의 종료시간보다 늦게 시작하는 회의 중에서, 회의가 가장 일찍 끝나는 회의로 이어간다

iter = input()

time_list = []
for _ in range(int(iter)):
    time = list(map(int, input().split()))
    time_list.append(time)

time_list.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간을 오름차순으로 정렬

end_time = 0
count = 0

for i in range(len(time_list)):
    if time_list[i][0] >= end_time:
        count += 1
        end_time = time_list[i][1]

print(count)