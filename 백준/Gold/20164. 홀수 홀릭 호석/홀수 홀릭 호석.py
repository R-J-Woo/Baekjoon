import sys
input = sys.stdin.readline

N = input().strip()

min_val = float('inf')
max_val = 0

def count_odd(s):
    return sum(1 for x in s if int(x) % 2 == 1)

def dfs(s, total):
    global min_val, max_val

    # 현재 숫자에서 홀수 개수 더하기
    total += count_odd(s)

    # 길이 1 → 종료
    if len(s) == 1:
        min_val = min(min_val, total)
        max_val = max(max_val, total)
        return

    # 길이 2 → 두 수 더하기
    if len(s) == 2:
        new_num = str(int(s[0]) + int(s[1]))
        dfs(new_num, total)
        return

    # 길이 3 이상 → 3등분
    for i in range(1, len(s)):
        for j in range(i + 1, len(s)):
            a = s[:i]
            b = s[i:j]
            c = s[j:]

            new_num = str(int(a) + int(b) + int(c))
            dfs(new_num, total)

dfs(N, 0)

print(min_val, max_val)