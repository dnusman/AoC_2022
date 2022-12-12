########################################################################################################################
def script(path_input):
    with open(path_input, 'r') as input_file:
        input = input_file.read().splitlines()

    # Part 1 & 2 #######################################################################################################
    count_part_1 = 0
    count_part_2 = 0
    for l in input:
        sections_all = l.split(',')
        sections_elf_1 = list(map(int, sections_all[0].split('-')))
        sections_elf_2 = list(map(int, sections_all[1].split('-')))
        sections_elf_1_all = set(range(sections_elf_1[0], sections_elf_1[1] + 1))
        sections_elf_2_all = set(range(sections_elf_2[0], sections_elf_2[1] + 1))

        count_part_1 += sections_elf_1_all.issubset(sections_elf_2_all) or \
                        sections_elf_2_all.issubset(sections_elf_1_all)
        count_part_2 += len(sections_elf_1_all.intersection(sections_elf_2_all)) > 0

    print(f'Solution part 1: {count_part_1}')
    print(f'Solution part 2: {count_part_2}')


########################################################################################################################
if __name__ == "__main__":
    script(path_input=f'../input/day_{__file__.split(".")[0][-1]}.txt')
