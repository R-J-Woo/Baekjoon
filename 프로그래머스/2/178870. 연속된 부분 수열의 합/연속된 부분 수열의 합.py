def solution(sequence, k):
    answer = [0, 0]
    min_length = float('inf')
    
    left = 0
    total = 0
    
    for right in range(len(sequence)):
        total += sequence[right]
        
        while total > k:
            total -= sequence[left]
            left += 1
        
        if total == k:
            if right - left < min_length:
                answer = [left, right]
                min_length = right - left
                
    return answer