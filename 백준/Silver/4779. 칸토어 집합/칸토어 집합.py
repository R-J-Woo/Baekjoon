def cantor(start, end, bar_list):
    length = int(end - start)
    if length <= 1:
        return
    else:
        for i in range(start + int(length / 3), start + 2 * int(length / 3)):
            bar_list[i] = " "

        cantor(start, start + int(length / 3), bar_list)
        cantor(start + int(2 * (length / 3)), end, bar_list)


while True:
    try:
        n = int(input())
        bar_list = ["-"] * (3 ** n)
        cantor(0, 3 ** n, bar_list)
        print(''.join(bar_list))
    except:
        break