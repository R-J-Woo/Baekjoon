def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5] * 2000
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    s3 = [3, 3, 1, 1, 2, 2, 4, 4 ,5, 5] * 1000
    correct = [0] * 3 # 1, 2, 3번 수포자가 맞춘 정답 수
    
    for i in range(len(answers)):
        if answers[i] == s1[i]:
            correct[0] += 1
        if answers[i] == s2[i]:
            correct[1] += 1
        if answers[i] == s3[i]:
            correct[2] += 1
            
    high = max(correct)
    
    for i in range(len(correct)):
        if correct[i] == high:
            answer.append(i+1)
    
    return answer