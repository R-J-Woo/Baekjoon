def solution(n, lost, reserve):
    
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    for student in range(1, n + 1):
        if student in lost and student in reserve:
            lost.remove(student)
            reserve.remove(student)
    
    for student in range(1, n + 1):
        # 체육복이 있으면
        if student not in lost:
            answer += 1
            continue
        # 체육복이 없으면
        else:
            # 우선 앞의 번호를 먼저 찾음
            if (student - 1) in reserve:
                answer += 1
                reserve.remove(student - 1)
            # 그 후 뒤의 번호를 찾음
            elif (student + 1) in reserve:
                answer += 1
                reserve.remove(student + 1)
            
    return answer;
            