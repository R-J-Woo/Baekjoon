# 아이디어: 스택을 이용
# 문장의 글자를 하나하나 추가해 가면서, 문장의 뒷 부분이 폭발 문자열과 같다면 삭제
# ex) mirkovC4의 뒷 부분이 폭발 문자열 C4와 같으므로 pop 두번 실행

word = input()
boom = input()

stack = []
for w in word:
    stack.append(w)
    length = len(boom)
    # 문장의 뒷 부분이 폭발 문자열과 같다면 폭발 문자열 길이만큼 pop
    if len(stack) >= length and ''.join(stack[-length:]) == boom:
        for _ in range(length):
            stack.pop()

if len(stack) > 0:
    print(''.join(stack))
else:
    print("FRULA")