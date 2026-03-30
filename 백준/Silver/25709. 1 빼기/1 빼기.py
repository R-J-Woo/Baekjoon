N = int(input())

result = 0
while N > 0:
    # 가지고 있는 수에서 1을 하나 지움
    if '1' in str(N):
        N = str(N)
        N = N.replace("1", "", 1) # 첫 번쨰 1만 제거

        if N == "":
            N = 0
        else:
            N = int(N) # 다시 숫자로 변환 -> 맨 앞의 연속되는 0 제거
    else:
        N -=  1

    result += 1

print(result)