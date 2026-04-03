N, M = map(int, input().split())

players = []
for _ in range(N):
    cards = list(map(int, input().split()))
    cards.sort(reverse=True)
    players.append(cards)

grade = [0] * N

for _ in range(M):
    max_value = 0
    
    # 이번 라운드 최대값
    for i in range(N):
        max_value = max(max_value, players[i][0])
    
    # 점수 추가
    for i in range(N):
        if players[i][0] == max_value:
            grade[i] += 1
    
    # 모든 플레이어 카드 제거
    for i in range(N):
        players[i].pop(0)

max_grade = max(grade)

result = []
for i in range(N):
    if grade[i] == max_grade:
        result.append(str(i + 1))

print(' '.join(result))