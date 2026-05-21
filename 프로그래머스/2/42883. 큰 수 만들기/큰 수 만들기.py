# 아이디어: 조합이나 순열을 이용하면 시간 초과 발생
# 스택을 이용해서 뒤의 숫자가 앞의 숫자보다 크면 스택에서 제거하고 숫자를 추가하는 방식으로 진행
from itertools import combinations

def solution(number, k):
    
    stack = []
    count = 0 # 제거한 숫자의 수
    
    for num in number:
        while stack and stack[-1] < num and count < k:
            stack.pop()
            count += 1
            
        stack.append(num)
        
    # 아직 k만큼 제거하지 못했다면 뒤에서 제거
    while count < k:
        stack.pop()
        count += 1
    
    return "".join(stack)