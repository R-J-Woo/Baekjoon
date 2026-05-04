def to_min(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(book_time):
    answer = 0
    
    book_time = [(to_min(s), to_min(e)) for s, e in book_time]
    book_time.sort()
    room = []
    
    for start, end in book_time:
        
        # 첫 번째 손님이면 방 하나 추가
        if len(room) == 0:
            room.append((start, end))
            answer = max(answer, len(room))
            continue
            
        # 첫 번째 손님이 아닌 경우 모든 방을 순회하면서 시간이 끝난 방이 있는지 탐색
        flag = False
        for i in range(len(room)):
            st, et = room[i]
            if et + 10 <= start:
                room[i] = start, end
                flag = True
                break
                
        # 시간이 끝난 방이 없으면 하나 추가
        if not flag:
            room.append((start, end))
            answer = max(answer, len(room))
        
        
    return answer