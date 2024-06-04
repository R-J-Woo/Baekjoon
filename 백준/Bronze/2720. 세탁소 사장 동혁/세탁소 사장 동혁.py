money_list = [25, 10, 5, 1]

iter = input()
iter = int(iter)

for i in range(iter):
    count_list = ""
    money = input()
    money = int(money)
    
    for m in money_list:
        n = money // m
        money %= m
        
        count_list += str(n) + ' '
    
    print(count_list)