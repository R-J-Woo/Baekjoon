from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    for i in range(len(numbers)):
        if i == 0:
            queue.append(numbers[i])
            queue.append((-1) * numbers[i])
        else:
            index = 0
            length = len(queue)
            while index < length:
                x = queue.popleft()
                queue.append(x + numbers[i])
                queue.append(x - numbers[i])
                index += 1
                
    while queue:
        x = queue.popleft()
        if x == target:
            answer += 1
        
    return answer