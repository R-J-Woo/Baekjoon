from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)
time = 0
current_weight = 0

while bridge:
    time += 1
    left = bridge.popleft()
    current_weight -= left

    if trucks:
        if current_weight + trucks[0] <= L:
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)

print(time)