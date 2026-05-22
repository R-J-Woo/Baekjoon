from itertools import permutations

def is_prime(number):
    if number <= 1:
        return False
    
    count = 0
    for i in range(2, number):
        if number % i == 0:
            count += 1
            
    if count == 0:
        return True
    else:
        return False
    

def solution(numbers):
    answer = 0
    
    number_set = set()
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            number = int("".join(perm))
            number_set.add(number)
            
    for num in number_set:
        if is_prime(num):
            answer += 1
    
    return answer