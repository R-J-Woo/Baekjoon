numbers = list(input())
numbers.sort(reverse=True)
print(''.join(str(num) for num in numbers))