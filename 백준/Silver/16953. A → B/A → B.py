# 문제 풀이
# 1을 떼면 자릿수가 빠르게 줄어들기 때문에 1을 떼는게 가능한지 먼저 확인하고, 그게 안되면 이후에 2로 나뉘어지는지 확인한다

l = list(input().split())
a, b = l[0], l[1]

count = 1
# 최종 값인 b에서 a가 되도록 역으로 연산한다
while True:
    # 두 개의 수가 같으면
    if a == b:
        print(count)
        break
    # b의 값이 a보다 작아지면
    elif int(b) < int(a):
        print(-1)
        break
    # 맨 끝자리가 1이면 1을 지워줌
    elif b[-1] == '1':
        b = b[:-1]
        count += 1
    # b가 2로 나뉘어지면 2로 나누어줌
    elif int(b) % 2 == 0:
        b = str(int(b) // 2)
        count += 1
    else:
        print(-1)
        break