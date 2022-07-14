# 아이디어: 1부터 시작해서 n을 생성하는 생성자를 구한다
n = int(input())

num = 1
while num <= n:
    l = []
    tmp = num
    while tmp // 10 != 0:  # 즉, num을 한 자리수 씩 분해하겠다는 뜻
        l.append(tmp % 10)
        tmp = tmp // 10
    else:
        l.append(tmp)

    result = sum(l) + num

    if result == n:
        print(num)
        break
    else:
        num += 1

else:  # 결국 생성자가 없는 경우에는
    print(0)
