from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    queue = deque()
    queue.append(1)
    visited = [0] * (n + 1)
    visited[1] = 1
    
    while queue:
        node = queue.popleft()
        
        for v in graph[node]:
            if visited[v] == 0:
                visited[v] = visited[node] + 1
                queue.append(v)
                
    for i in range(1, n + 1):
        if max(visited) == visited[i]:
            answer += 1
    
    return answer