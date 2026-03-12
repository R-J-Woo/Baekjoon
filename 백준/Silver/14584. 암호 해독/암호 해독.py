code = input()
N = int(input())

words = []
for _ in range(N):
    words.append(input())

for shift in range(26):
    decoded = ""

    for c in code:
        decoded += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))

    for word in words:
        if word in decoded:
            print(decoded)
            exit()