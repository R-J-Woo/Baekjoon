import itertools

a = int(input())
numList = list(map(int, input().split()))
operand = ['+', '-', 'x', '/']
cList = list(map(int, input().split()))
operList = []

for i in range(len(cList)):
  for _ in range(cList[i]):
    operList.append(operand[i])

# 모든 순열 조합을 생성
operList = list(itertools.permutations(operList))

results = []

for l1 in operList:
  result = numList[0]
  for i in range(len(l1)):
    if l1[i] == '+':
      result += numList[i+1]
    elif l1[i] == '-':
      result -= numList[i+1]
    elif l1[i] == 'x':
      result *= numList[i+1]
    else:
      if result < 0:
        result = -1 * result
        result //= numList[i+1]
        result = -1 * result
      else:
        result //= numList[i+1]

  results.append(result)
  
print(max(results))
print(min(results))