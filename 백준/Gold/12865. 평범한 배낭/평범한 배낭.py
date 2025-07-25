# 아이디어: 다이나믹 프로그래밍 이용

n, k = map(int, input().split())
wv = []
for _ in range(n):
    wv.append(list(map(int, input().split())))

wv.sort()

k_list = [0] * (k + 1)
for i in range(n):
    # 오름차순으로 하면 중복 사용이 있을 수 있기 때문에 내림차순으로 순회
    for j in range(k, wv[i][0] - 1, -1):
        if j == wv[i][0]:
            k_list[j] = wv[i][1]
        # 만들 수 있는 무게의 경우 가치의 최댓값 비교
        elif k_list[j - wv[i][0]] != 0:
            k_list[j] = max(k_list[j], k_list[j - wv[i][0]] + wv[i][1])

print(max(k_list[1:]))