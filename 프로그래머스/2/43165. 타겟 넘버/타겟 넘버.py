from collections import deque

def solution(numbers, target):
    
    queue = deque()
    queue.append((numbers[0], 1))
    queue.append((-numbers[0], 1))
    
    answer = 0
    while queue:
        value, count = queue.popleft()
        
        # 모든 숫자를 사용했을 경우
        if count == len(numbers):
            if value == target:
                answer += 1
            continue
        
        queue.append((value + numbers[count], count + 1))
        queue.append((value - numbers[count], count + 1))
        
    return answer