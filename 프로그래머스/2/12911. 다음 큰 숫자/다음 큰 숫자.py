def one_count(binary):
    count = 0
    for b in binary:
        if b == "1":
            count += 1
            
    return count


def get_binary(number):
    binary = ""
    while number > 0:
        num = number % 2
        number //= 2
        binary += str(num)
        
    return binary
    

def solution(n):
    answer = 0
    
    binary = get_binary(n)
    count = one_count(binary)
    for num in range(n + 1, 1000001):
        temp_binary = get_binary(num)
        temp_count = one_count(temp_binary)
        if count == temp_count:
            answer = num
            break
    
    return answer