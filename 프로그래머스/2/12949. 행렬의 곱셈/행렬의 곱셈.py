def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            row = arr1[i]
            col = [row[j] for row in arr2]
            
            value = 0
            for k in range(len(row)):
                value += row[k] * col[k]
                
            answer[i][j] = value
    
    return answer