def solution(answers):
    
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = [0, 0, 0]
    for i in range(len(answers)):
        # 1번 수포자 확인
        if answers[i] == student1[i % 5]:
            count[0] += 1
        
        # 2번 수포자 확인
        if answers[i] == student2[i % 8]:
            count[1] += 1
        
        # 3번 수포자 확인
        if answers[i] == student3[i % 10]:
            count[2] += 1
        
    # 가장 높은 점수를 받은 사람 구하기
    answer = []
    for i in range(3):
        if max(count) == count[i]:
            answer.append(i + 1)
    
    return answer