# code for part 1
with open('rucksack.txt', 'r') as fh:
    # set up
    # priority a=1 to z=26 A=27 to Z=52
    priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []


    # load the file and make a list without newline character
    temp_read_in = fh.read()
    temp_read_in = temp_read_in.split()

    # count the length of the character and split this in the middle
    for i in temp_read_in:
        looper = False
        first_half = i[:len(i) // 2]
        second_half = i[(len(i)+1) // 2:]
        # compare is a character in both sections
        for j in first_half:
            for k in second_half:
                if not looper:
                    if j == k:
                        for x in range(len(priority)):
                            if k == priority[x]:
                                hit = (k, x+1)
                                # if yes store this result with the priority value in a list
                                result.append(hit)
                                looper = True
                        break



    # calculate the sum of all priorities from the result list
    all_results = 0
    for v in result:
        all_results = v[1] + all_results
    print(all_results)




