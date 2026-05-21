def solution(people, limit):
    answer = 0
    
    people.sort()
    left, right = 0, len(people) - 1
    
    # 가장 가벼운 사람과 가장 무거운 사람을 묶어서 태움
    while left < right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            answer += 1
            right -= 1
            
    if left == right:
        answer += 1
        
    return answer