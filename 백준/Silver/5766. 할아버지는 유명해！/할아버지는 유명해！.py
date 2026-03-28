while True:
    N, M = map(int, input().split())

    # 프로그램 종료 조건
    if N == 0 and M == 0:
        break

    player = {}
    score = set()
    for _ in range(N):
        rank = list(map(int, input().split()))
        for num in rank:
            if num in player:
                player[num] += 1
                score.add(player[num])
            else:
                player[num] = 1
                score.add(1)

    scores = list(player.values())
    unique_scores = sorted(set(scores), reverse=True)
    second = unique_scores[1]

    result = []
    for key in sorted(player):
        if player[key] == second:
            result.append(str(key))

    print(' '.join(result))

    