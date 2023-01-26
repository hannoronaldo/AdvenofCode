# code for part 2
# import re
answer = ''

with open("signaling.txt", 'r') as fh:
    signal = fh.read()

    for i in range(14, len(signal)):
        temp_set = set(signal[i-14:i])
        if len(temp_set) == 14:
            answer = i


print(answer)


