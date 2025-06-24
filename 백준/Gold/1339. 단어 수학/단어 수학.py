# 아이디어: 각 알파벳의 자리수별 기여값(weight) 를 모두 더한 뒤, 이 weight가 큰 알파벳에 큰 숫자를 부여
# 즉, 단어가 여러 개 있고, 각 알파벳이 여러 자리수에 걸쳐 등장할 수 있기 때문에 단순히 자리수 순서대로 부여하면 최적이 아닙니다

import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

alpha = {}

# 각 알파벳별 가중치 계산
for word in words:
    length = len(word)
    for i, char in enumerate(word):
        if char in alpha:
            alpha[char] += 10 ** (length - i - 1)
        else:
            alpha[char] = 10 ** (length - i - 1)

# 가중치가 큰 알파벳 순으로 정렬
weights = sorted(alpha.values(), reverse=True)

# 큰 숫자부터 곱해서 합산
num = 9
total = 0
for weight in weights:
    total += weight * num
    num -= 1

print(total)
