def solution(n):
    answer = ''
    
    numbers = ['1', '2', '4']
    
    while n > 0:
        idx = (n - 1) % 3
        n = (n - 1) // 3
        answer = numbers[idx] + answer
    
    return answer