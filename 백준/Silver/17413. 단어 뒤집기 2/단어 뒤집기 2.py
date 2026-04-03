s = input()

answer = ""
start = 0
for i in range(len(s)):
    if s[i] == "<":
        answer += ''.join(reversed(s[start:i]))
        start = i
    elif s[i] == ">":
        answer += s[start:i + 1]
        start = i + 1
    elif s[i] == " ":
        if s[start] != "<":
            answer += ''.join(reversed(s[start:i])) + " "
            start = i + 1
    elif i == len(s) - 1:
        answer += ''.join(reversed(s[start:]))

print(answer)