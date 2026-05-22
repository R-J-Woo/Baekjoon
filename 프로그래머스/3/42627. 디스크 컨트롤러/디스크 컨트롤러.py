import heapq

def solution(jobs):
    
    jobs.sort()
    total = 0
    
    ready = []
    time = 0
    idx = 0
    while idx < len(jobs) or ready:
            
        # 현재 시간까지 요청된 작업 삽입
        while idx < len(jobs) and jobs[idx][0] <= time:
            start, spend = jobs[idx]
            heapq.heappush(ready, (spend, start))
            idx += 1
           
        # 큐에 대기하는 작업이 있다면
        if ready:
            spend, start = heapq.heappop(ready)
            time += spend
            total += (time - start)
        else:
            time += 1
            
        
    
    return total // len(jobs)