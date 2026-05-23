def solution(elements):
    num_set = set()

    # 배열의 길이를 2배로 늘려서 원형 수열 대비
    n = len(elements)
    elements = elements * 2

    for length in range(1, n + 1):
        for start in range(n):
            value = sum(elements[start:start+length])
            num_set.add(value)

    return len(num_set)