# code for part 2
import re
result = 0
result_overlap = 0
result_range = 0
result_none = 0
with open('cleaning_area.txt', 'r') as fh:

    # set up


    result = 0
    # load the file and make a list without newline character
    for line in fh:
        cords = line.rstrip().split(',')
        x1, y1 = list(map(int, cords[0].split('-')))
        x2, y2 = list(map(int, cords[1].split('-')))
        if (x1 in range(x2, y2+1) or y1 in range(x2, y2+1)) or \
                (x2 in range(x1, y1 + 1) or y2 in range(x1, y1 + 1)):
            result_overlap += 1
        elif (x1 <= x2 and y2 <= y1) or (x2 <= x1 and y1 <= y2):
            result_range += 1
        else:
            result_none += 1
    result = result_overlap + result_range
    print(result)


