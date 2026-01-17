# 아이디어: 브루트포스 -> 햄버거의 개수를 최소부터 최대까지 순회하면서 값을 갱신

n, m, t = map(int, input().split())
time = [n, m]
time.sort()

max_burger = 0
min_coke = t
for i in range((t // time[0]) + 1):
    temp_t = t
    burger = 0

    # 시간이 짧은 버거
    burger += i
    temp_t -= (time[0] * i)
    
    # 시간이 긴 버거
    burger += (temp_t // time[1])
    temp_t %= time[1]

    # 콜라 마시는 시간
    coke = temp_t

    if coke <= min_coke and burger > max_burger:
        max_burger = burger
        min_coke = coke

print(max_burger, min_coke)