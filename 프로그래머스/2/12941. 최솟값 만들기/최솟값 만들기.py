def solution(A,B):
    answer = 0

    # A와 B에서 작은 값과 큰 값을 골라서 곱한 후 더하면 최솟값
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        value = A[i] * B[i]
        answer += value

    return answer