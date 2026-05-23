def solution(s):
    answer = ''
    
    s = list(s)
    
    for i in range(len(s)):
        # 단어의 첫 글자
        if i == 0 or s[i-1] == " ":
            # 소문자라면 대문자로 변환
            if 'a' <= s[i] <= 'z':
                s[i] = chr(ord(s[i]) - 32)
        # 그 외 글자
        else:
            if 'A' <= s[i] <= 'Z':
                s[i] = chr(ord(s[i]) + 32)
                
    answer = "".join(s)
    
    return answer