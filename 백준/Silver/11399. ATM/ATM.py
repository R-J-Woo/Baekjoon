person = int(input())
time_list = list(map(int, input().split()))

time_list.sort()

time_count = 0
for i in range(len(time_list)):
    time_count += sum(time_list[:i+1])
    
print(time_count)