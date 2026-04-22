import heapq

def solution(scoville, K):
    
    # 스코빌이 낮은 순서대로 삽입
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
        
    answer = 0
    while len(heap) > 1:
        # 가장 낮은 음식의 스코빌 지수가 K를 넘는다면 종료
        h1 = heapq.heappop(heap)
        if h1 >= K:
            return answer
            
        h2 = heapq.heappop(heap)
            
        new_h = h1 + (h2 * 2)
        heapq.heappush(heap, new_h)
        answer += 1
        
    # 마지막 하나 남았을 때
    if heap[0] >= K:
        return answer
    else:
        return -1