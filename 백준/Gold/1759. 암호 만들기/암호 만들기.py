from itertools import combinations

L, C = map(int, input().split())
alphas = list(input().split())

result = []
for password in combinations(alphas, L):
    password = list(password)
    a, b = 0, 0
    for p in password:
        if p in ('a', 'e', 'i', 'o', 'u'):
            b += 1
        else:
            a += 1
    
    # 최소 한 개의 모음과 최소 두 개의 자음이 없다면 건너뜀
    if not (b >= 1 and a >= 2):
        continue

    # 오름차순으로 정렬
    password.sort()
    pwd = ''.join(password)

    # 처음 나온 비밀번호만 추가
    if pwd not in result:
        result.append(pwd)

result.sort()
for r in result:
    print(r)