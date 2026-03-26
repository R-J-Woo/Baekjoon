def dfs(idx, correct, answer):
    global result

    # 가지치기 ⭐
    if correct + (10 - idx) < 5:
        return

    # 끝까지 다 찍었으면
    if idx == 10:
        if correct >= 5:
            result += 1
        return

    for i in range(1, 6):
        # 3연속 방지
        if len(answer) >= 2 and answer[-1] == i and answer[-2] == i:
            continue

        answer.append(i)

        # 정답 여부 반영
        if i == collect[idx]:
            dfs(idx + 1, correct + 1, answer)
        else:
            dfs(idx + 1, correct, answer)

        answer.pop()


result = 0
collect = list(map(int, input().split()))

dfs(0, 0, [])
print(result)