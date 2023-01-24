# code for part 1
import re
result = 0
with open('cleaning_area.txt', 'r') as fh:

    for lines in fh:
        cords = lines.rstrip().split(',')
        x1, y1 = list(map(int, cords[0].split('-')))
        x2, y2 = list(map(int, cords[1].split('-')))
        if (x1 <= x2 and y2 <= y1) or \
                (x2 <= x1 and y1 <= y2):
            result += 1
print(result)





