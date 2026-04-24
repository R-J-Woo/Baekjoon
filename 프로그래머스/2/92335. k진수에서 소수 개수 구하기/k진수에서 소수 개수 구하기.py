def get_knum(number, k):
    knum = ""
    while number > 0:
        num = number % k
        number //= k
        knum += str(num)
        
    return knum[::-1]

    
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True
    
    
def solution(n, k):
    answer = 0
    
    # k 진수 변환
    knum = get_knum(n, k)
    knum = knum.split("0")
    
    for x in knum:
    	# x가 비어있는 경우를 예외처리
        if x and isPrime(int(x)):
            answer += 1
        
    return answer