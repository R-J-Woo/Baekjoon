# 아이디어: A를 B의 시작점을 달리 하면서 비교함 -> 차이가 최소가 되는 지점을 찾으면 됨 (어차피 길이가 달라도 같은 문자를 추가한다는 가정을 하면 차이가 없게 되므로, 같은 길이에서 비교)

A, B = input().split()
result = 50
for i in range(len(B) - len(A) + 1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            count += 1

    result = min(result, count)

print(result)