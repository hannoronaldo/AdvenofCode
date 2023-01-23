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
'''    # set up
    fall1 = 0
    fall2 = 0
    block_counter = 0
    result = 0
    # load the file and make a list without newline character
    temp_read_in = fh.read()
    temp_read_in = re.split(r"\W+", temp_read_in)
    for i in range(0, len(temp_read_in), 4):
        x1 = temp_read_in[i]
        y1 = temp_read_in[i+1]
        x2 = temp_read_in[i+2]
        y2 = temp_read_in[i+3]
        block_counter = block_counter + 1

        # check for is first block fully covered in second bloc or vice versa
        if (x1 <= x2 and y2 <= y1) or \
                (x2 <= x1 and y1 <= y2):
            if x2 >= x1 and y2 <= y1:
                fall1 = fall1 + 1  # range2 is in range1
            elif x1 >= x2 and y1 <= y2:
                fall2 = fall2 + 1  # range1 is in range2
            result = result + 1
    print(result)
'''





