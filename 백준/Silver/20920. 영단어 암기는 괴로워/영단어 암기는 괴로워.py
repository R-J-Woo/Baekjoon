import sys
input = sys.stdin.readline

words = []
word_dict = {} # 단어가 나온 횟수 저장 -> 매번 리스트를 갱신하면 시간 복잡도 상승

n, m = map(int, input().split())
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        # 이미 나온 단어라면
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            words.append([1, len(word), word]) # 나온 횟수, 단어 길이, 단어 순으로 저장

# 나온 횟수 저장
for l in words:
    word = l[2]
    l[0] = word_dict[word]

# 나온 횟수, 단어 길이는 내림차순, 단어는 오름차순 정렬
words.sort(key=lambda x: (-x[0], -x[1], x[2]))
for word in words:
    print(word[2])