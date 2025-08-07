n, k = map(int, input().split())
numbers = list(input())

count = 0
stack = []
for number in numbers: # O(N)
    while len(stack) > 0 and count < k and stack[-1] < number:
        stack.pop()
        count += 1

    stack.append(number)

# 끝까지 돌았는데도 삭제 횟수를 채우지 못했을 경우 부족한 삭제 횟수만큼 뒤에서 제거
if count < k:
    stack = stack[:-(k-count)]

print(''.join(str(s) for s in stack))
