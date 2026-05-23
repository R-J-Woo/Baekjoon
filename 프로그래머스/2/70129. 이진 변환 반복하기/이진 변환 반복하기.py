import math

def binary_transform(s):
    s = list(s)
    x = []
    zero_count = 0
    
    # s의 모든 0을 제거
    for i in range(len(s)):
        if s[i] == "0":
            zero_count += 1
        else:
            x.append(s[i])
    
    # 2진법으로 표현한 문자열로 변환
    c = len(x)
    binary = ""
    end = math.floor(math.log2(c))
    for i in range(end, -1, -1):
        if 2 ** i <= c:
            binary += "1"
            c -= 2 ** i
        else:
            binary += "0"
        
    return binary, zero_count
    

def solution(s):
    answer = []
    
    count = 0
    zero = 0
    while s != "1":
        count += 1
        s, zero_count = binary_transform(s)
        zero += zero_count
        
    answer = [count, zero]
    
    return answer