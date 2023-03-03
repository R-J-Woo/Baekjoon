def solution(n, lost, reserve):
    lost.sort()
    delete_num = []
    
    for lostStudent in lost:
        if lostStudent in reserve:
            delete_num.append(lostStudent)
            
    for num in delete_num:
        lost.remove(num)
        reserve.remove(num)
            
    answer = n - len(lost)
            
    for lostStudent in lost:
        if (lostStudent - 1) in reserve:
            answer += 1
            reserve.remove(lostStudent - 1)
        elif (lostStudent + 1) in reserve:
            answer += 1
            reserve.remove(lostStudent + 1)
            
    return answer