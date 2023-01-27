# code for part 1
file_system = {}
with open ("day7_small.in", 'r') as fh:
    action = fh.read().split('\n')
    directory = ''
    set_ls = 0
    for step in action:
        command = step.split(' ')
        if len(command) == 3:  # if so -> change dir
            directory = command[2]
            if directory in file_system:
                pass
            else:
                file_system[directory]
            break
        elif command[1] == 'ls': # if so -> list di
                set_ls = 1
        else:
            if set_ls:
                file_system[directory] = (command[0], command[1]) # write all items to dict

    print(action)
https://www.youtube.com/watch?v=FXQWIWHaFBE
