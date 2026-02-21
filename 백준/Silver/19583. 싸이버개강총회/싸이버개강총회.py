import sys
input = sys.stdin.readline

S, E, Q = input().split()

start = set()
end = set()
while True:
    info = input().strip()

    if not info:
        break

    time, person = info.split()

    if time <= S:
        start.add(person)

    if E <= time <= Q and person in start:
        end.add(person)


print(len(end))