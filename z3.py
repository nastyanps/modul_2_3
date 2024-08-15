my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while True:
    start = my_list[0]
    if start > 0:
        res = my_list.pop(0)
        print(res)
    if start == 0:
        my_list.pop(0)
        continue
    if start < 0 or len(my_list) == 0:
        break

