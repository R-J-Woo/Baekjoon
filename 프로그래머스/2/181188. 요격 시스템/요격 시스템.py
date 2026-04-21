def solution(targets):
    # 끝나는 지점 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    
    count = 0
    last = -1  # 마지막 요격 위치
    
    for start, end in targets:
        # 현재 요격으로 커버 불가능하면
        if start >= last:
            count += 1
            last = end
            
    return count