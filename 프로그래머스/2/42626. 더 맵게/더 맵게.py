import heapq

def solution(scoville, K):
    
    # 매운 음식을 낮은 순서부터 빼기 위해 우선순위큐에 삽입
    spicy = []
    for s in scoville:
        heapq.heappush(spicy, s)
        
    answer = 0 # 섞는 횟수
    while True:
        s1 = heapq.heappop(spicy)
        
        # 모든 음식의 스코빌 지수가 K 이상인 경우
        if s1 >= K:
            break
            
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(spicy) == 0:
            answer = -1
            break
            
        s2 = heapq.heappop(spicy)
        new_scoville = s1 + s2 * 2
        heapq.heappush(spicy, new_scoville)
        answer += 1
    
    return answer