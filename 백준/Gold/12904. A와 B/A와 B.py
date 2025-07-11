s = input()
t = input()

flag = False
while len(t) >= len(s): # O(N)
    # s와 t가 같다면 종료
    if s == t:
        flag = True
        break

    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1] # O(N)

if flag == True:
    print(1)
else:
    print(0)