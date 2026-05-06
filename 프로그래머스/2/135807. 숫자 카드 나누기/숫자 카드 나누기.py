from math import gcd
from functools import reduce

# 최대 공약수 구하기
def get_gcd(arr):
    return reduce(gcd, arr)

# 최대 공약수로 나누어지는지 확인
def check(g, arr):
    for x in arr:
        if x % g == 0:
            return False
    return True

def solution(arrayA, arrayB):
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)
    
    answer = 0
    
    if check(gcdA, arrayB):
        answer = gcdA
        
    if check(gcdB, arrayA):
        answer = max(answer, gcdB)
        
    return answer