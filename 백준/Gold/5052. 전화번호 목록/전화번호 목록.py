import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = [input().strip() for _ in range(n)]
    numbers.sort()  # 사전순 정렬 -> 접두어 관계가 있을 수 있는 경우는 반드시 인접한 두 개 사이에만 존재하게 됨

    consistent = True
    for i in range(n - 1): # 정렬된 전화번호 리스트롤 돌면서 앞과 뒤의 전화번호를 비교
        if numbers[i+1].startswith(numbers[i]):
            consistent = False
            break

    print("YES" if consistent else "NO")
