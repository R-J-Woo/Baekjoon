# 아이디어1 - 30의 배수인 수를 만들고 싶다면, 반드시 1의 자리에 0이 존재해야 함 -> 입력받은 수에 0이 없다면 실패 처리
# 아이디어2 - 3의 배수인 수는 각 자리의 수를 합쳐도 3의 배수가 나온다는 것을 이용 -> 입력받은 수에서 0을 뗀 후에 3의 배수가 되는지 확인
# 아이디어3 - 3의 배수가 된다면, 높은 숫자 순서대로 정렬해서 숫자 생성 -> 가장 큰 숫자 완성

import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))

if 0 not in n: # 0이 없으면 실패
    print(-1)
elif sum(map(int, n)) % 3 != 0: # 각 자리 수의 합이 3의 배수가 아니면 실패
    print(-1)
else:
    n.sort(reverse=True) # 내림차순으로 정렬
    num = ''.join(map(str, n))
    print(num)
    