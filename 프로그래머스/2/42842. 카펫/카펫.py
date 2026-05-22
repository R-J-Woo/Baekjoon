def solution(brown, yellow):
    answer = [0, 0]
    
    for i in range(3, brown):
        for j in range(3, i + 1):
            total = i * j
            b = 2 * i + 2 * j - 4
            y = total - b
            if brown == b and yellow == y:
                answer = [i, j]
                break
            
    return answer