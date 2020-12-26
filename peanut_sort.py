def peanut_sort(first_number, last_number):
    i = 0
    num = []
    num.append(first_number) # 첫번째 넘버 넣기. 1이라면 1 append
    num.append(last_number - 1) # 마지막 넘버 넣기. 10이라면 10 - 1 = 9 append
    
    first_num = int(first_number + 1)
    las_num = int(last_number - 2)
    num.append(first_num)
    num.append(las_num)

    while last_number > i:
        first_num = first_num + 1
        num.append(first_num)

        las_num = las_num - 1
        num.append(las_num)
        
        i = i + 1
        if 0 in num:
            break

    print(num)
