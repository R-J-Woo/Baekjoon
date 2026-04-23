from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    wants = {}
    for i in range(len(want)):
        wants[want[i]] = number[i]
        
    for i in range(len(discount) - 9):
        count = Counter(discount[i:i+10])
        
        flag = True
        for item in wants:
            if count[item] != wants[item]:
                flag = False
                break
                
        if flag:
            answer += 1
            
    
    return answer