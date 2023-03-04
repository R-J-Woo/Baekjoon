a = int(input())
coin_list = [500, 100, 50, 10, 5, 1]

money = 1000 - a
count = 0
for coin in coin_list:
    if coin <= money:
        count += money // coin
        money %= coin
        
print(count)