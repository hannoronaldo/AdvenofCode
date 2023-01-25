# code for part 1
# import re
answer = ''

with open("signaling.txt", 'r') as fh:
    signal = fh.read()

    for i in range(0, len(signal)):
        flag_1to4 = 0
        flag_is5equal_to1to4 = 0
        char1 = signal[i]
        char2 = signal[i+1]
        char3 = signal[i+2]
        char4 = signal[i+3]
        char5 = signal[i+4]
        if char1 == char2 or char2 == char3 or char3 == char4 or char1 == char3 or char2 == char4 or char1 == char4:
            flag_1to4 = 1
        if char5 == char1 or char5 == char2 or char5 == char3 or char5 == char4:
            flag_is5equal_to1to4 = 1
        if not flag_1to4 and not flag_is5equal_to1to4:
            answer += str(i+4) + ','


print(answer)
