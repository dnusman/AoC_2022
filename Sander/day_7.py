import re
import pandas as pd

path_input=f'../input/day_{__file__.split(".")[0][-1]}.txt'

with open(path_input, 'r') as input_file:
    input = input_file.read().splitlines()

# Part 1 #######################################################################################################
filesystem = {}
path = ()

for l in input:
    if l[0] == '$':  # Command (ls is ignored, it comes before adding content)
        command = l.split(' ')[1]
        if command == 'cd':
            dir = l.split(' ')[-1]
            if dir == '..':  # Move one up, so remove last element of path
                path = path[:-1]
            else:
                path += (dir,)  # cd to dir, so add to path
                if dir not in filesystem.keys():  # If path content does not exist yet, create it
                    filesystem[path] = {'superior_dirs': path[:-1] if dir != '/' else '', 'content': []}
    else:  # Add content
        filesystem[path]['content'] += [l]

# Sort path lengths, so size of inferior directories can be added to superior ones
sorted_paths = pd.DataFrame([[k, len(k)] for k in filesystem.keys()], columns=['dir', 'depth'])
sorted_paths = sorted_paths.sort_values('depth', ascending=False)

for d in sorted_paths['dir'].to_list():
    total_size = 0
    for e in filesystem[d]['content']:  # For every entry in content
        if e[:3] == 'dir':  # If a directory, grab it's total size
            total_size += filesystem[d + (e.split(' ')[-1],)]['total_size']  # Make sure to add current dir to path
        else:
            size = re.findall(r'\d+', e)  # Find file size
            total_size += int(size[0])  # And add to total
    filesystem[d]['total_size'] = total_size  # Overwrite total

# List dirs and sizes
all_sizes = pd.DataFrame([[k, v['total_size']] for k, v in filesystem.items()], columns=['dir', 'total_size'])
answer_part_1 = all_sizes[all_sizes['total_size'] <= 100000]['total_size'].sum()
print(f'Solution part 1: {answer_part_1}')

# Part 2 #######################################################################################################
unused_space = 70000000 - all_sizes[all_sizes['dir'] == ('/',)]['total_size'][0]  # As cannot delete root
space_to_delete = 30000000 - unused_space  # Find difference to required space
all_sizes = all_sizes.sort_values('total_size')  # Sort ascending
dir_to_delete = all_sizes[all_sizes['total_size'] > space_to_delete].iloc[0, :]  # Grab first one which meets requiremnt
answer_part_2 = dir_to_delete['total_size']
print(f'Solution part 2: {answer_part_2}')
