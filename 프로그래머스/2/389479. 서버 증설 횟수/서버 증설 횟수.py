from collections import deque

def solution(players, m, k):
    answer = 0
    
    queue = deque()
    server = 0
    
    for time in range(len(players)):
        player = players[time]
        
        # 만료된 서버 전부 제거
        while queue and queue[0][0] + k <= time:
            server -= queue[0][1]
            queue.popleft()
            
        # 필요한 서버 수
        required = player // m
        
        # 부족한 만큼 증설
        if required > server:
            count = required - server
            answer += count
            server += count
            queue.append((time, count))
    
    return answer