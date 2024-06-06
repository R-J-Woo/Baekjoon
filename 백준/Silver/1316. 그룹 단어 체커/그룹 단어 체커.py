iter = int(input())

str_list = []

# 입력받기
for _ in range(iter):
    string = input()
    str_list.append(string)


count = 0
for string in str_list:
    count_flag = True
    start_str = string[0]
    for i in range(len(string)):
        if start_str != string[i]:
            if string[i:].find(start_str) != -1: # 그 뒤에도 문자가 남아있으면
                count_flag = False
                break
            start_str = string[i]

    if count_flag == True:
        count += 1
        

print(count)