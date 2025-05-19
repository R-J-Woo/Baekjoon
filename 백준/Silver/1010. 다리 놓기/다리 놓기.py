import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    count = math.comb(m, n)

    print(count)