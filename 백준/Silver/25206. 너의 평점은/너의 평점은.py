ratings = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0
          , 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
total_credit = 0
total_rating = 0
for _ in range(20):
    subject, credit, rating = input().split()

    if rating == 'P':
        continue

    total_credit += float(credit)
    total_rating += float(credit) * ratings[rating]

print(round(total_rating / total_credit, 6))