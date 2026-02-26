X = int(input())
N = int(input())

alps = []
result = {}
for _ in range(N):
    staff, score = input().split()
    score = int(score)

    # 5% 미만 정당 제외
    if score < X * 0.05:
        continue

    for i in range(1, 15):
        num = score / i
        alps.append((num, staff))
        result[staff] = 0

# 높은 숫자부터 정렬
alps.sort(reverse=True)

for i in range(14):
    num, staff = alps[i]
    result[staff] += 1

for key in sorted(result):
    print(key, result[key])