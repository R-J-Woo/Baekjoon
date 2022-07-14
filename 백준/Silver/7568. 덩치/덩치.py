# 아이디어 처음부터 차례대로 비교해본다
n = int(input())
w = []  # 몸무게
h = []  # 키
count = 0
while count < n:
    weight, height = input().split()
    w.append(int(weight))
    h.append(int(height))
    count += 1

rank = []
for i in range(len(w)):
    larger = 0  # 덩치가 더 큰 사람의 수
    for j in range(len(w)):
        if w[i] < w[j] and h[i] < h[j]: # 덩치가 더 크면
            larger += 1

    rank.append(larger + 1)

for r in rank:
    print(r, end=' ')
