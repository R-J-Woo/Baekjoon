N = int(input())
nums = list(map(int, input().split()))

result = 0
for i in range(N-3):
    for j in range(i+1, N-2):
        for k in range(j+1, N-1):
            a = 1
            for x in nums[:i+1]:
                a *= x

            b = 1
            for x in nums[i+1:j+1]:
                b *= x

            c = 1
            for x in nums[j+1:k+1]:
                c *= x

            d = 1
            for x in nums[k+1:]:
                d *= x

            result = max(result, a+b+c+d)

print(result)