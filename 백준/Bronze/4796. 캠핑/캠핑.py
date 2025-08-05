import sys
input = sys.stdin.readline

case_count = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    result = l * (v // p) + min(v % p, l)
    print("Case " + str(case_count) + ": " + str(result))
    case_count += 1