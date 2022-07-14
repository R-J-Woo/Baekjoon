# 아이디어: 3장 합의 모든 경우의 수를 구해서 m을 넘지 않으면서 m에 가장 가까운 합을 출력한다
n, m = input().split()
n = int(n)
m = int(m)

num_list = list(map(int, input().split()))
sum = []

for n1 in num_list:
    for n2 in num_list:
        for n3 in num_list:
            if n1 == n2 or n1 == n3 or n2 == n3:  # 같은 숫자가 있으면
                break
            else:
                sum.append(n1+n2+n3)

underM = []
for s in sum:
    if s <= m:  # m을 넘지 않는 값을 저장
        underM.append(s)

print(max(underM))
