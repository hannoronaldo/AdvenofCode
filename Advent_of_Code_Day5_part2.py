# code for part 2
# import re
answer = ''
manal_inst = ['move 4 from 2 to 1', 'move 1 from 6 to 9', 'move 6 from 4 to 7',
              'move 1 from 2 to 5', 'move 3 from 6 to 3', 'move 4 from 3 to 9']
with open("supply_stack.txt", 'r') as fh:
    stack_strings, instructions = (i.splitlines() for i in fh.read().strip("\n").split("\n\n"))
    stacks = {int(digit): [] for digit in stack_strings[-1].replace(" ", "")}
    indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]


    def display_stack():
        print('Stack content' + '\n')
        for item in stacks:
            print(item, stacks[item])
        print('\n')

    def loadStacks():

        for string in stack_strings[:-1]:
            stack_counter = 0
            sl = len(string)

            for index in indexes:
                stack_counter += 1
                if index >= sl:
                    break
                if string[index] != ' ':
                    stacks[stack_counter].insert(0, string[index])

    def resort_stack():
        inst = [i.split() for i in instructions]
        for i in inst:
            count = int(i[1])
            start = int(i[3])
            target = int(i[5])
            for loop in range(count):
                temp_pop = stacks[start].pop()
                stacks[target].append(temp_pop)

        print(stacks)

    def resort_stack_9001():
        inst = [i.split() for i in instructions]
        for i in inst:
            count = int(i[1])
            start = int(i[3])
            target = int(i[5])
            if count == 1:
                temp_pop = stacks[start].pop()
                stacks[target].append(temp_pop)
            else:
                start_pos = len(stacks[start]) - count
                for char in range(start_pos, len(stacks[start])):
                    stacks[target].append(stacks[start][char])
                for k in range(count):
                    stacks[start].pop()
        print(stacks)




    loadStacks()
    #resort_stack()
    resort_stack_9001()
    #display_stack()
for items in stacks:
    answer += stacks[items][-1]

print(answer)


