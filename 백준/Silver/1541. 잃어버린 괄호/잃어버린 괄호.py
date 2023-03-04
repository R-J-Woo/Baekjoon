strA = input()
strList = []

# 00009같이 이상한 데이터를 대비하여 데이터 전처리 진행
lastSymbol = 0
for i in range(len(strA)):
    if strA[i] in ('+', '-'):
        strList.append(int(strA[lastSymbol:i]))
        strList.append(strA[i])
        lastSymbol = i + 1
        continue
        
    if i == len(strA) - 1:
        strList.append(int(strA[lastSymbol:]))

strList2 = []
for a in strList:
    strList2.append(a)
    if strList2[len(strList2) - 2] == '+': # 예를 들어 [9, '+', 4]의 상황이라면
        n1 = strList2.pop()
        strList2.pop()
        n2 = strList2.pop()
        strList2.append(n1+n2)

answer = strList2[0]
for i in range(1, len(strList2)):
    if strList2[i] != '-':
        answer -= strList2[i]
        
print(answer)