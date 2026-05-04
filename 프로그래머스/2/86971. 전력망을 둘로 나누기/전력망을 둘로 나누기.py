from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    count = 0
    while queue:
        count += 1
        node = queue.popleft()
        
        for v in graph[node]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                
    return count


def solution(n, wires):
    answer = float('inf')
    
    for cut in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        
        # 하나를 끊고 전력망 생성
        for i in range(len(wires)):
            if i == cut:
                continue
            
            x, y = wires[i]
            graph[x].append(y)
            graph[y].append(x)
            
        count = []
        for i in range(1, n + 1):
            if not visited[i]:
                value = bfs(graph, i, visited)
                count.append(value)
                
        answer = min(answer, abs(count[0] - count[1]))
        
    
    return answer