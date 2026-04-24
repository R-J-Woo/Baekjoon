from collections import Counter

def solution(topping):
    answer = 0
    
    # 토핑의 개수 세기 -> 시작할 때는 오른쪽에만 모든 토핑이 있음
    left, right = {}, Counter(topping)
    
    for i in range(len(topping)):
        ingredient = topping[i]
        
        # 왼쪽에 토핑 추가
        if ingredient not in left:
            left[ingredient] = 1
        else:
            left[ingredient] += 1
            
        # 오른쪽에서 토핑 제거
        if right[ingredient] == 1:
            del right[ingredient]
        else:
            right[ingredient] -= 1
            
        if len(left) == len(right):
            answer += 1
        
    
    return answer