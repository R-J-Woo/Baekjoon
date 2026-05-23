from collections import deque
import math

# 두 수의 최소 공배수 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    answer = 0
    arr.sort()
    
    queue = deque()
    for num in arr:
        queue.append(num)
        
    while len(queue) >= 2:
        a = queue.popleft()
        b = queue.popleft()
        c = lcm(a, b)
        queue.append(c)
        
    answer = queue.popleft()
    return answer