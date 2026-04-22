def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        idx = 0
        flag = True
        for t in tree:
            if t in skill:
                if idx >= len(skill) or t != skill[idx]:
                    flag = False
                    break
                idx += 1
                
        if flag:
            answer += 1
            
    return answer