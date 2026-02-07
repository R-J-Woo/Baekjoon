T = int(input())
for _ in range(T):
    n = int(input())
    votes = []
    for _ in range(n):
        votes.append(int(input()))

    total = sum(votes)
    max_vote = max(votes)
    vote_count = 0
    vote_idx = 0
    for i in range(len(votes)):
        if votes[i] == max_vote:
            vote_idx = i
            vote_count += 1

    # 최다 득표자가 1명 초과
    if vote_count > 1:
        print("no winner")
    else:
        # 과반수
        if total < (max_vote * 2):
            print("majority winner", vote_idx + 1)
        else:
            print("minority winner", vote_idx + 1)