S = input()

counter = {}
for c in S:
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1

result = 0

def dfs(word, length):
    global result

    if length == len(S):
        result += 1
        return
    
    for char in counter:
        if counter[char] > 0 and (word == "" or char != word[-1]):
            counter[char] -= 1
            dfs(word + char, length + 1)
            counter[char] += 1

dfs("", 0)
print(result)