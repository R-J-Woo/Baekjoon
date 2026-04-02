n = int(input())
max_birth = "99999999"
min_birth = "00000000"
oldest = ""
youngest = ""
for _ in range(n):
    name, day, month, year = input().split()
    
    if len(day) < 2:
        day = '0' + day
    if len(month) < 2:
        month = '0' + month

    birthday = year + month + day
    if birthday < max_birth:
        max_birth = birthday
        oldest = name

    if birthday > min_birth:
        min_birth = birthday
        youngest = name

print(youngest)
print(oldest)