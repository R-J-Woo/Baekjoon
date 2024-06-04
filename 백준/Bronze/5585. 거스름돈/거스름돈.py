money = int(input())
remain = 1000 - money
count = 0

money_list = [500, 100, 50, 10, 5, 1]

for m in money_list:
    count += remain // m
    remain %= m
    
print(count)