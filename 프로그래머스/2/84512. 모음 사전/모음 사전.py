from itertools import permutations

def solution(word):
    answer = 0
    alphas = ['A', 'E', 'I', 'O', 'U'] * 5
    
    # 사전 만들기
    books = []
    book_set = set()
    for i in range(1, 6):
        for perm in permutations(alphas, i):
            book = "".join(perm)
            if book not in book_set:
                books.append(book)
                book_set.add(book)
                
    books.sort()
    
    return books.index(word) + 1