A = int(input())
T = int(input())
answer = int(input())

result = 0
b, d = 0, 0
for i in range(2, 10000):
    seq = ['뻔', '데기', '뻔', '데기']
    seq += ['뻔'] * i
    seq += ['데기'] * i

    for s in seq:
        if s == '뻔':
            b += 1
        else:
            d += 1

        result += 1

        if (answer == 0 and b == T) or (answer == 1 and d == T):
            print((result - 1) % A)
            exit()