from collections import Counter

n = int(input())
participants = [input().strip() for _ in range(n)]
finishers = [input().strip() for _ in range(n-1)]

counter = Counter(participants)

for finisher in finishers:
    counter[finisher] -= 1

for person, count in counter.items():
    if count > 0:
        print(person)
        break
