import string


########################################################################################################################
def script(path_input):
    with open(path_input, 'r') as input_file:
        input = input_file.read().splitlines()

    # Part 1 ###########################################################################################################
    priority = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    sum_part_1 = 0
    for l in input:
        first_comp = l[:int(len(l) / 2)]
        second_comp = l[int(len(l) / 2):]
        same_item = set(first_comp).intersection(set(second_comp))
        sum_part_1 += priority.index(list(same_item)[0]) + 1

    print(f'Solution part 1: {sum_part_1}')

    # Part 2 ###########################################################################################################
    sum_part_2 = 0
    group_total = []
    for i, l in enumerate(input):
        i += 1
        group_total += [l]

        if i % 3 == 0:
            same_item = set(group_total[0]).intersection(set(group_total[1])).intersection(group_total[2])
            sum_part_2 += priority.index(list(same_item)[0]) + 1
            group_total = []

    print(f'Solution part 2: {sum_part_2}')


########################################################################################################################
if __name__ == "__main__":
    script(path_input=f'../input/day_{__file__.split(".")[0][-1]}.txt')
