def dfs(player, total):
    global answer
    
    # 11명 다 배치 완료
    if player == 11:
        answer = max(answer, total)
        return
    
    for position in range(11):
        if not visited[position] and ability[player][position] != 0:
            visited[position] = True
            dfs(player + 1, total + ability[player][position])
            visited[position] = False


T = int(input())
for _ in range(T):
    ability = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    answer = 0
    
    dfs(0, 0)
    print(answer)