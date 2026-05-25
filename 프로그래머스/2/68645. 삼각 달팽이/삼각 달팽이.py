def solution(n):
    answer = []
    
    snail = [[0] * n for _ in range(n)]
        
    direction = ["down", "right", "up"]
    dir_idx = -1    # 방향 찾는 인덱스
    x, y = -1, 0     # 현재 달팽이의 위치
    num = 0         # 달팽이에 넣을 숫자
    
    for count in range(n, 0, -1):
        
        # 움직일 방향 찾기
        dir_idx = (dir_idx + 1) % 3
        d = direction[dir_idx]
        
        # 숫자 채우기
        if d == "down":
            for _ in range(count):
                x += 1
                num += 1
                snail[x][y] = num
        elif d == "up":
            for _ in range(count):
                x -= 1
                y -= 1
                num += 1
                snail[x][y] = num
        elif d == "right":
            for _ in range(count):
                y += 1
                num += 1
                snail[x][y] = num
            
    for row in snail:
        for num in row:
            if num == 0:
                break
            answer.append(num)
    
    return answer