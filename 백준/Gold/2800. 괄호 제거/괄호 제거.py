from itertools import combinations

string = input()

# 괄호의 짝을 구하기
brackets = []
stack = []
for i in range(len(string)):
    if string[i] == '(':
        stack.append(i)
    elif string[i] == ')':
        left = stack.pop()
        right = i
        brackets.append([left, right])

# 1~괄호 짝의 개수까지 조합하면서, 출력에서 제외할 괄호의 인덱스 짝을 구함
# 중복 제거를 위해 집합을 사용
total_result = set()
for count in range(1, len(brackets) + 1):
    for c in combinations(brackets, count):
        total_brackets = []
        for i in range(count):
            total_brackets.append(c[i][0])
            total_brackets.append(c[i][1])

        result = ''
        for i in range(len(string)):
            if i not in total_brackets:
                result += string[i]

        total_result.add(result)

# 사전 순으로 정렬
total_result = list(sorted(total_result))
for result in total_result:
    print(result)