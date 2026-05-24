from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    # LRU 알고리즘 사용을 위해 큐 활용
    cache = deque()
    
    for city in cities:
        # 대소문자 구분을 하지 않기 때문에 대문자로 통일
        city = city.upper()
        
        # cache hit
        if city in cache:
            answer += 1
            # 최신 사용으로 갱신
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.popleft()
                cache.append(city)
    
    return answer