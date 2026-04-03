T = int(input())

for _ in range(T):
    S = input()
    
    result = ""
    for i in range(len(S)):
        ex = S[:i]
        temp = S + ex[::-1]
        if temp == temp[::-1]:
            result = temp
            break

    print(result)