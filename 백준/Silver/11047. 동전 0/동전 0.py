n, k = input().split()
n = int(n)
k = int(k)
l1 = []
c = 0
while c < n:  # 동전의 가치 입력
    a = int(input())
    l1.append(a)
    c += 1

l2 = []
for num in l1:  # k보다 작은 가치를 가진 동전만 담기
    if num <= k:
        l2.append(num)
count = 0
for i in range(len(l2)):
    count += k // l2[(-1)*i-1]
    k %= l2[(-1)*i-1]

print(count)
