from collections import deque

def bfs(computers, i, visited):
    queue = deque()
    queue.append(i)
    visited[i] = True
    
    while queue:
        node = queue.popleft()
        
        for idx in range(len(computers[node])):
            if computers[node][idx] == 1 and not visited[idx]:
                visited[idx] = True
                queue.append(idx)
    

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(computers, i, visited)
    
    return answer