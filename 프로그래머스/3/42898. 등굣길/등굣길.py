def solution(m, n, puddles):
    answer = 0
    
    maps = [[0] * n for _ in range(m)]
    for x, y in puddles:
        maps[x-1][y-1] = 1
        
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    for x in range(m):
        for y in range(n):
            # 시작 위치는 건너뜀
            if x == 0 and y == 0:
                continue
            
            # 장애물도 건너뜀
            if maps[x][y] == 1:
                continue
                
            value = 0
            if x > 0:
                value += dp[x-1][y]
            if y > 0:
                value += dp[x][y-1]
                
            dp[x][y] = value
    
    return dp[m-1][n-1] % 1000000007