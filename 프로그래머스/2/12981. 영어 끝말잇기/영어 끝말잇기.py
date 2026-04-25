def solution(n, words):
    answer = [0, 0]

    count = 0
    words_set = set()
    
    for i in range(len(words)):        
        # 한바퀴 다 돌면 count += 1
        if i % n == 0:
            count += 1
            
        # 이전에 나왔던 단어인 경우
        word = words[i]
        if word in words_set:
            answer = [(i % n) + 1, count]
            break
            
        # 앞 단어와 끝글자와 이어지지 않는 경우
        if i > 0 and words[i-1][-1] != word[0]:
            answer = [(i % n) + 1, count]
            break
            
        words_set.add(word)

    return answer