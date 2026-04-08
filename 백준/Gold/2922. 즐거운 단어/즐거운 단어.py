word = input()
N = len(word)

vowels = {'A', 'E', 'I', 'O', 'U'}

def dfs(idx, v_cnt, c_cnt, has_l):
    # 3개 연속이면 탈락
    if v_cnt >= 3 or c_cnt >= 3:
        return 0

    # 끝까지 왔을 때
    if idx == N:
        return 1 if has_l else 0

    result = 0
    char = word[idx]

    # 이미 문자 있는 경우
    if char != '_':
        if char in vowels:
            result += dfs(idx + 1, v_cnt + 1, 0, has_l)
        else:
            result += dfs(idx + 1, 0, c_cnt + 1, has_l or char == 'L')
    
    # '_'인 경우
    else:
        # 1. 모음 선택 (5가지)
        result += 5 * dfs(idx + 1, v_cnt + 1, 0, has_l)

        # 2. 자음 선택 (L 제외 20개)
        result += 20 * dfs(idx + 1, 0, c_cnt + 1, has_l)

        # 3. L 선택 (1개)
        result += dfs(idx + 1, 0, c_cnt + 1, True)

    return result

print(dfs(0, 0, 0, False))