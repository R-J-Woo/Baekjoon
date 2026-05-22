from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for comb in permutations(dungeons):
        hp = k    # 피로도
        count = 0 # 던전 수
        
        for need, spend in comb:
            if need > hp: # 최소 필요 피로도가 남은 피로도보다 크면 종료
                break
                
            hp -= spend
            count += 1
            
        answer = max(answer, count)
    
    return answer