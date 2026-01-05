# 그리디 알고리즘
# - 각 DNA 순서에서 글자가 가장 많이 일치하는 DNA를 선택
# - ex) 예제1에서는 첫번째 글자는 T가 가장 많으므로 T, 두번째 글자는 A가 가장 많으므로 A ... 이런식으로 선택해나간다
# - 만약 글자의 등장 수가 모두 같다면 사전순으로 가장 앞서도록 한다

import sys
input = sys.stdin.readline

N, M = map(int, input().split())


# dna 입력받기
dnas = []
for _ in range(N):
    dnas.append(input().strip())

result = ""
count = 0
for i in range(M):
    counts = {}   
    # 각 글자가 나오는 횟수 확인 
    for dna in dnas:
        if dna[i] not in counts:
            counts[dna[i]] = 1
        else:
            counts[dna[i]] += 1

    # 가장 많이 나오는 글자 추출 / 횟수가 동일하면 사전 순
    a = ""
    num = 0
    for key in counts.keys():
        if num < counts[key]:
            a = key
            num = counts[key]
        elif num == counts[key]:
            a = min(a, key)
    result += a

    # 글자가 다른 수 확인
    for dna in dnas:
        if dna[i] != a:
            count += 1


print(result)
print(count)