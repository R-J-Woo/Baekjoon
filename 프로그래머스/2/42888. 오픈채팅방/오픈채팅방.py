def solution(record):
    answer = []
    
    match = {}
    for row in record:
        row = row.split()
        if len(row) < 3:
            continue

        move, uid, name = row
        match[uid] = name
        
    for row in record:
        row = row.split()
        move = row[0]
        uid = row[1]
        final_name = match[uid]
        
        if move == "Enter":
            answer.append(final_name + "님이 들어왔습니다.")
        elif move == "Leave":
            answer.append(final_name + "님이 나갔습니다.")
    
    return answer