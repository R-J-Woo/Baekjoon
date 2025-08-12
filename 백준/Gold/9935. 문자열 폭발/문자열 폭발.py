word = input()
boom = input()

stack = []
for w in word:
    stack.append(w)
    length = len(boom)
    if len(stack) >= length and ''.join(stack[-length:]) == boom:
        for _ in range(length):
            stack.pop()

if len(stack) > 0:
    print(''.join(stack))
else:
    print("FRULA")