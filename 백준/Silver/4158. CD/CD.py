import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:  # 종료 조건
        break
    
    cd1 = {int(input()) for _ in range(n)}
    cd2 = {int(input()) for _ in range(m)}
    
    # 교집합 크기 계산
    print(len(cd1 & cd2))