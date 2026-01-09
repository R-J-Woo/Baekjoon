import sys
input = sys.stdin.readline

string = input().strip()
length = len(string)
comb = []

for i in range(1, length - 1):
    for j in range(i + 1, length):
        a = string[:i][::-1]
        b = string[i:j][::-1]
        c = string[j:][::-1]
        new_string = a + b + c
        comb.append(new_string)

comb.sort()

print(comb[0])