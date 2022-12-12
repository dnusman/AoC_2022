toggle_example = True
path_input = f'../input/day_{__file__.split(".")[0].split("_")[-1]}{"_example" if toggle_example else ""}.txt'

with open(path_input, 'r') as input_file:
    input = input_file.read().splitlines()

all_monkeys = {}

for l in input:
    if l == '':  # Monkey characteristics are delimited with new line, skip
        continue
    elif l.startswith('Monkey'):
        monkey = l.split(':')[0].strip()  # Get the monkey name
        all_monkeys[monkey] = {}  # Add to dict of monkeys
    else:
        attribute = l.split(':')[0].strip()  # Get monkey characteristic
        value = l.split(':')[1].strip()  # And its value

        if attribute == 'Starting items':  # Convert the starting items from str to int
            value = list(map(int, value.split(', ')))
        elif attribute == 'Test':  # And the testing value as well
            value = int(value.split(' ')[-1])

        all_monkeys[monkey][attribute] = value  # Add characteristic to monkey

for m in all_monkeys.keys():  # Also initialize inspection counter for every monkey
    all_monkeys[m]['Inspections'] = 0

max_rounds = 20

for r in range(1, max_rounds + 1):  # Loop over rounds
    for m in all_monkeys.keys():  # Loop over all monkeys
        for old in all_monkeys[m]['Starting items']:  # Loop over all starting items a monkey has at start of round
            all_monkeys[m]['Inspections'] += 1  # Add one inspection to the count
            exec(all_monkeys[m]['Operation'])  # Execute the monkey operation
            # new = math.floor(new / 3)
            test_result = new % all_monkeys[m]['Test']  # Perform if divisible by testing value
            if test_result == 0:  # If true, look-up next monkey
                new_monkey = f'Monkey {all_monkeys[m]["If true"].split(" ")[-1]}'
            else:  # Same if false
                new_monkey = f'Monkey {all_monkeys[m]["If false"].split(" ")[-1]}'

            # # If you mod with the test value of the new monkey, the test result will stay the same
            new = new % all_monkeys[new_monkey]['Test']

            all_monkeys[new_monkey]['Starting items'] += [new]  # Add item to starting items of new monkey
            all_monkeys[m]['Starting items'] = all_monkeys[m]['Starting items'][1:]  # Remove item from current monkey

inspections = [all_monkeys[m]['Inspections'] for m in all_monkeys.keys()]  # Select all inspection counters
max_inspections = sorted(inspections, reverse=True)[:2]  # Sort and grab maximum two
answer = max_inspections[0] * max_inspections[1]  # Multiply for answer
