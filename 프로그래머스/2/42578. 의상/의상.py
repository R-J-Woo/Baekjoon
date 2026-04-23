def solution(clothes):
    answer = 0
    
    total = {}
    for cloth in clothes:
        if cloth[1] not in total:
            total[cloth[1]] = [cloth[0]]
        else:
            total[cloth[1]].append(cloth[0])
            
    if len(total) == 1:
        answer = len(clothes)
    else:
        result = 1
        for key in total:
            result *= (len(total[key]) + 1)
        answer = result - 1
    
    return answer