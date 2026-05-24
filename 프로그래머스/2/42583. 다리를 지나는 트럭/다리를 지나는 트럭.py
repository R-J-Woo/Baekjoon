from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    trucks = deque()
    for truck in truck_weights:
        trucks.append(truck)
    
    bridge = deque()
    for _ in range(bridge_length):
        bridge.append(0)
        
    truck_count = 0  # 현재 다리 위의 트럭 수
    truck_weight = 0 # 현재 다리 위의 무게
    total_truck = 0  # 다리를 지난 트럭의 개수
    
    while total_truck < len(truck_weights):
        answer += 1
        
        ##### 다리 위의 트럭 하나 건너기 #####
        t = bridge.popleft()
        if t > 0:
            truck_count -= 1
            truck_weight -= t
            total_truck += 1
            
        ##### 다리 위에 트럭 하나 추가 #####
        
        # 더 올릴 수 없는 트럭이 없다면
        if len(trucks) == 0:
            bridge.append(0)
            continue
            
        w = trucks[0]
        if truck_weight + w <= weight and truck_count < bridge_length: # 무게를 견딜 수 있고 최대 트럭 수 이하라면 추가 가능
            t = trucks.popleft()
            bridge.append(t)
            truck_count += 1
            truck_weight += t
        else: # 트럭을 올릴 수 없다면
            bridge.append(0)
            
    
    return answer