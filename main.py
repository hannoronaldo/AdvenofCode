# code for part 1
import pprint
file_system = {}
with open("day7_small.in", 'r') as fh:
    action = fh.read().split('\n')
    actual_directory = ''

    parent_directory = ''

    set_ls = 0
    path = ''
    for step in action:

        if step[0] == '$' and step[2:4] == 'cd':  # if so -> change dir
            actual_directory = step[5:]

            if actual_directory == '..':  # go back to parent directory
                path = parent_directory
            elif not parent_directory:
                parent_directory = actual_directory
                path = actual_directory
                file_system[parent_directory] = {}
            else:

                path = actual_directory
                temp_dict = {path: []}
                file_system[parent_directory] = temp_dict


            set_ls = 0
        elif step[0] == '$' and step[2:4] == 'ls':
            set_ls = 1
        else:
            if set_ls:
                if step[:3] == 'dir':
                    path_name = step[4:]
                    file_system[parent_directory][path_name] = []  # write all items to dict
                else:
                    file_found = step.split(' ')
                    file_system.update(file_found)
    pprint.pprint(file_system.items())

