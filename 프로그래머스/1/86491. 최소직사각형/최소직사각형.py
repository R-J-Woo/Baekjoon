def solution(sizes):
    answer = 0
    
    # 가능한 모든 가로, 세로 길이를 담음
    length = []
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
            
    max_w, max_h = 0, 0
    for size in sizes:
        max_w = max(max_w, size[0])
        max_h = max(max_h, size[1])
    
    return max_w * max_h