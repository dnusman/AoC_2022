import pandas as pd


########################################################################################################################
def script(path_input):
    with open(path_input, 'r') as input_file:
        input = input_file.read().splitlines()

    input_split = input.index('')
    stack_positions = list(range(1, len(input[input_split - 2]), 4))  # Determine from last row of stacks

    starting_stacks = pd.read_fwf(path_input, header=None, nrows=input_split - 1,
                                  colspecs=[(p, p + 1) for p in stack_positions],
                                  names=list(range(1, len(stack_positions) + 1)))
    procedure = pd.read_csv(path_input, header=None, skiprows=input_split + 1, delimiter=' ')[[1, 3, 5]]
    procedure.columns = ['amount', 'from', 'to']

    starting_stacks = starting_stacks.to_dict(orient='list')
    starting_stacks = {k: [c for c in v if isinstance(c, str)] for k, v in starting_stacks.items()}  # Drop nan's

    # Part 1 ###########################################################################################################
    stacks_part_1 = starting_stacks.copy()
    for _, row in procedure.iterrows():  # For every action
        for a in range(1, row['amount'] + 1):
            top_crate = stacks_part_1[row['from']][0]  # Determine top crate
            stacks_part_1[row['from']] = stacks_part_1[row['from']][1:]  # Remove top crate from first stack
            stacks_part_1[row['to']] = [top_crate] + stacks_part_1[row['to']]  # Add top crate to second stack

    top_crates_part_1 = ''.join([s[0] for s in stacks_part_1.values()])

    print(f'Solution part 1: {top_crates_part_1}')

    # Part 2 ###########################################################################################################
    stacks_part_2 = starting_stacks.copy()
    for _, row in procedure.iterrows():
        top_crates = stacks_part_2[row['from']][:row['amount']]  # Determine x top crates
        stacks_part_2[row['from']] = stacks_part_2[row['from']][len(top_crates):]  # Remove from first stack
        stacks_part_2[row['to']] = top_crates + stacks_part_2[row['to']]  # Add to second stack

    top_crates_part_2 = ''.join([s[0] for s in stacks_part_2.values()])

    print(f'Solution part 2: {top_crates_part_2}')


########################################################################################################################
if __name__ == "__main__":
    script(path_input=f'../input/day_{__file__.split(".")[0][-1]}.txt')
