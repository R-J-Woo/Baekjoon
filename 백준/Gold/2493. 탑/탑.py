# 아이디어: stack을 사용
# stack이 비어있지 않다면, 현재 탐색 중인 stack의 top과 비교하여 현재 탐색 중인 탑이 더 크면 pop
# stack이 비거나 그렇지 않은 탑이 나올 때까지 반복
# 위 과정이 끝나면 현재 탑을 push하고 다음 탑

from sys import stdin

N = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
stk = []
answers = ['0'] * N

for i in range(N-1, -1, -1):
    while stk and towers[i] >= stk[-1][1]:
        answers[stk.pop()[0]] = str(i+1)	# 수신하는 탑 번호 기록
    stk.append((i, towers[i]))

print(" ".join(answers))