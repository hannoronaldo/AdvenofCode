elf_dict = {}
with open('data.txt', 'r') as fh:
    temp_readin = fh.read()
    data_readin = temp_readin.split('\n')
    temp_list = []
    counter = 1
    for i in data_readin:
        if i:
            temp_list.append(i)
        else:
            max_calories = sum(int(i) for i in temp_list)
            name = 'elf' + str(counter)
            elf_dict[name] = max_calories
            counter = counter + 1
            temp_list = []
    elf_max_col_list = []
    for i, j in elf_dict.items():
        short = (j, i)
        elf_max_col_list.append(short)
    elf_list_sort = sorted(elf_max_col_list)
    helper = elf_list_sort[-3:]
    max_cal = helper[0][0] + helper[1][0] + helper[2][0]
    print(elf_list_sort[-3:])

