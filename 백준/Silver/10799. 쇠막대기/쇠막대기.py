word = input()

stack = []
count = 0
for i in range(len(word)):
    if word[i] == "(":
        stack.append(word[i])
    elif word[i] == ")" and word[i-1] == "(": # 레이저
        stack.pop()
        count += len(stack)
    elif word[i] == ")" and word[i-1] != "(": # 레이저가 아닌 쇠막대기가 끝나는 경우
        stack.pop()
        count += 1

print(count)