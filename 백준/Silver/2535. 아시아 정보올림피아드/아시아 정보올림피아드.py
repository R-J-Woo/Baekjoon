N = int(input())
st = []
nation_medal = {}
for _ in range(N):
    nation, student, grade = map(int, input().split())
    st.append((grade, nation, student))
    if nation not in nation_medal:
        nation_medal[nation] = 0

st.sort(reverse=True) # 점수 내림차순으로 정렬
medal = []
for s in st:
    if len(medal) >= 3:
        break

    # 이미 2개 이상 메달을 가지지 않은 나라만 수여
    if nation_medal[s[1]] < 2:
        medal.append((s[1], s[2]))
        nation_medal[s[1]] += 1

for m in medal:
    print(m[0], m[1])