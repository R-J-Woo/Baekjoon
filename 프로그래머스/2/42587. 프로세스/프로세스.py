from collections import deque

def solution(priorities, location):
    answer = 0
    
    p_queue = deque()
    l_queue = deque()
    
    for i in range(len(priorities)):
        p_queue.append(priorities[i])
        l_queue.append(i)
    
    while p_queue:
        p = p_queue.popleft()
        l = l_queue.popleft()
        
        if not p_queue or p >= max(p_queue):
            answer += 1
            if l == location:
                break
        else:
            p_queue.append(p)
            l_queue.append(l)
    
    return answer