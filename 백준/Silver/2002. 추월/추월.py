N = int(input())
daegun = [input() for _ in range(N)]
youngsik = [input() for _ in range(N)]

# 입구 순서 → 번호 매기기
order = {car: i for i, car in enumerate(daegun)}

# 출구 순서를 번호로 변환
out = [order[car] for car in youngsik]

count = 0

for i in range(N):
    for j in range(i + 1, N):
        if out[i] > out[j]:  # 뒤에 들어온 차가 먼저 나옴
            count += 1
            break  # 한 번이라도 추월하면 카운트

print(count)