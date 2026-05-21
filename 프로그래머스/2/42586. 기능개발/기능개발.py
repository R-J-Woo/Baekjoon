def solution(progresses, speeds):
    answer = []
    
    idx = 0
    for day in range(1, 100):
        
        # 모든 작업이 완료되면 종료
        if idx >= len(progresses):
            break
        
        count = 0
        for i in range(idx, len(progresses)):
            p, s = progresses[idx], speeds[idx]
            if p + s * day >= 100:
                count += 1
                idx += 1
            else:
                break
                
        if count > 0:
            answer.append(count)
        
    
    return answer