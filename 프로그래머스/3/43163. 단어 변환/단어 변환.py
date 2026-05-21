from collections import deque

def can_transform(begin, target):
    count = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            count += 1
            
    if count == 1:
        return True
    else:
        return False
    

def solution(begin, target, words):
    answer = 0
    
    # words 안에 target이 없는 경우
    if target not in words:
        return answer

    queue = deque()
    queue.append((begin, 0)) # 단어, 변환 횟수
    visited = [False] * len(words)
    
    while queue:
        word, count = queue.popleft()
        
        if word == target:
            answer = count
            break
        
        for i in range(len(words)):
            # 만약 한 개의 알파벳을 바꿔서 변환할 수 있고, 아직 변환된 적이 없는 단어인 경우
            if can_transform(word, words[i]) and not visited[i]:
                visited[i] = True
                queue.append((words[i], count + 1))
    
    return answer