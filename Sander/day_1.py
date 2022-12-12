########################################################################################################################
def script(path_input):
    with open(path_input, 'r') as input_file:
        input = input_file.readlines()

    # Part 1 ###########################################################################################################
    cal_tot = 0
    cal_elf = []
    for l in input:
        if l == '\n':
            cal_elf += [cal_tot]
            cal_tot = 0
        else:
            cal_tot += int(l[:-1])

    cal_max = max(cal_elf)
    elf_max = cal_elf.index(cal_max)

    print(f'Solution part 1: {cal_max}')

    # Part 2 ###########################################################################################################
    top_3 = sorted(cal_elf, reverse=True)[:3]
    cal_tot_top_3 = sum(top_3)

    print(f'Solution part 12: {cal_tot_top_3}')


########################################################################################################################
if __name__ == "__main__":
    script(path_input=f'../input/day_{__file__.split(".")[0][-1]}.txt')
