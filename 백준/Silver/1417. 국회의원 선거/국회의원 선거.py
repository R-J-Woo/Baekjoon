N = int(input())
p = []
for _ in range(N):
    p.append(int(input()))

result = 0
while True:
    max_idx = 0
    for i in range(1, len(p)):
        if p[max_idx] <= p[i]:
            max_idx = i

    if max_idx == 0:
        break

    result += 1
    p[max_idx] -= 1
    p[0] += 1

print(result)