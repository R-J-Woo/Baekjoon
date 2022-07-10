i = int(input())
m = 1000 - i
c = 0

c += m // 500
m %= 500
c += m // 100
m %= 100
c += m // 50
m %= 50
c += m // 10
m %= 10
c += m // 5
m %= 5
c += m // 1

print(c)
