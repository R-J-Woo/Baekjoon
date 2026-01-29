from itertools import permutations
import math

def is_prime(number):
    if number <= 1:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    
    return True


c = int(input())
numbers = []
for _ in range(c):
    num = input()
    
    num_set = set()
    for i in range(1, len(num) + 1):
        for n in permutations(num, i):
            n = ''.join(n)
            num_set.add(int(n))

    count = 0
    for n in num_set:
        if is_prime(n):
            count += 1

    print(count)