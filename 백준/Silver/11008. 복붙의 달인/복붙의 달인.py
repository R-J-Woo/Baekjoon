T = int(input())

for _ in range(T):
    s, p = input().split()

    length = len(p)

    idx = 0
    result = 0
    while idx < len(s):
        if s[idx:idx+length] == p:
            idx += length
        else:
            idx +=1

        result += 1

    
    print(result)