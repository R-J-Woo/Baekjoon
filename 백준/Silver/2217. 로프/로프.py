
# idea: 병렬로 중량을 분산한다 하더라도 가장 낮은 무게를 버틸 수 있는 로프가 기준이기 때문에
# 고른 로프 중 가장 낮은 무게 * 로프의 갯수로 중량을 구하면 될 것 같다


iter = input()
iter = int(iter)

weight_list = []
for i in range(iter):
    weight = input()
    weight_list.append(int(weight))

weight_list.sort() # 오름차순으로 정렬

max_weight = []
max_weight.append(max(weight_list)) # 입력한 무게 중 가장 큰 무게를 입력

for i in range(len(weight_list)):
    max_weight.append(weight_list[i] * (len(weight_list) - i)) # 고른 로프 중 가장 낮은 무게 * 로프의 갯수

print(max(max_weight))
