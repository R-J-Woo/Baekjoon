N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    books = list(map(int, input().split()))
 
    boxs = 1
    temp = 0
    for book in books:
        temp += book
        if temp > M:
            boxs += 1
            temp = book
 
    print(boxs)