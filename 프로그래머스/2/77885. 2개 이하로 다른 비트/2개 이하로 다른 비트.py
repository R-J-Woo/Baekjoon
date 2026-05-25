def solution(numbers):
    answer = []

    for number in numbers:
        # 아이디어
        # 짝수 → 마지막 비트가 0 => 그냥 +1 하면 비트 1개만 달라짐
        # 홀수 → 가장 오른쪽의 0을 찾아서 => 01 → 10 으로 바꾸면 비트 2개만 달라지면서 가장 작음

        # 짝수
        if number % 2 == 0:
            answer.append(number + 1)

        # 홀수
        else:
            bit = '0' + bin(number)[2:]

            idx = bit.rfind('0')

            bit = list(bit)
            bit[idx] = '1'
            bit[idx + 1] = '0'

            answer.append(int(''.join(bit), 2))

    return answer