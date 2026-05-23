from collections import deque

def solution(s):
    answer = 0
    
    # 큐로 만들어서 문자열을 회전
    queue = deque()
    for c in s:
        queue.append(c)
        
    for _ in range(len(s)):
        c = queue.popleft()
        queue.append(c)
        
        # 올바른 괄호 문자열인지 판단
        stack = []
        for i in range(len(queue)):
            if queue[i] in ("[", "(", "{"):
                stack.append(queue[i])
            else:
                if len(stack) > 0 and stack[-1] == "[" and queue[i] == "]":
                    stack.pop()
                elif len(stack) > 0 and stack[-1] == "(" and queue[i] == ")":
                    stack.pop()
                elif len(stack) > 0 and stack[-1] == "{" and queue[i] == "}":
                    stack.pop()
                else:
                    stack.append(queue[i])
                    
        if len(stack) == 0:
            answer += 1
        
    return answer