words = []
while True:
    word = input()
    if word == ".":
        break
    words.append(word)

for word in words:
    stack = []
    balanced = True
    for w in word:
        if w == "(" or w == "[":
            stack.append(w)
        elif w == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                balanced = False
                break
        elif w == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                balanced = False
                break

    if balanced and len(stack) == 0:
        print("yes")
    else:
        print("no")
