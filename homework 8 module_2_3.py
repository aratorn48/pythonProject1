my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list):
    index_num = my_list[index]
    index += 1
    if index_num < 0:
        break
    if index_num > 0:
        print(index_num)


