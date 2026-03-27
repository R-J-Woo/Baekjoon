import sys
input = sys.stdin.readline

n = int(input())

check = [0 for _ in range(n*2)]
max_res = 0
cnt = 0
for i in list(map(int,input().split())):
    if not check[i]:
        cnt+=1
        max_res = max(cnt,max_res)
        check[i] = 1
    else:
        cnt-=1
        
print(max_res)