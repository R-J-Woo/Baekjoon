def solution(n, times):
    answer = max(times) * n
    left, right = 0, max(times) * n
    
    while left <= right:
        # 중간 값으로 시간 세팅 후, 몇명을 심사할 수 있는지 확인
        mid = (left + right) // 2
        count = 0
        for time in times:
            count += mid // time
            
        if count >= n:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
        
    return answer