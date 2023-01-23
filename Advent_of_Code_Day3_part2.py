# code for part 2

def find_tag(fb, sb, tb):
    looper = 0
    for j in fb:
        for k in sb:
            for p in tb:
                if not looper:
                    if j == k and j == p:
                        for x in range(len(priority)):
                            if k == priority[x]:
                                hit = (k, x + 1)
                                # if yes store this result with the priority value in a list
                                result.append(hit)
                                looper = True
                        break


with open('rucksack.txt', 'r') as fh:
    # set up
    # priority a=1 to z=26 A=27 to Z=52
    priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []

    # load the file and make a list without newline character
    temp_read_in = fh.read()
    temp_read_in = temp_read_in.split()
    counter = 0  # help counter for line number

    # calculate length of loop
    loop_counter = len(temp_read_in)
    # read in 3 blocks
    for i in range(0, len(temp_read_in), 3):
        first_block = temp_read_in[i]
        second_block = temp_read_in[i + 1]
        third_block = temp_read_in[i + 2]
        find_tag(first_block, second_block, third_block)
    print(result)
    # compare is a character in both sections

    # calculate the sum of all priorities from the result list
    all_results = 0
    for v in result:
        all_results = v[1] + all_results
    print(all_results)




