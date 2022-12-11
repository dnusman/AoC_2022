import re
with open("input") as f:
    data = f.read()

r = re.compile(r"Monkey \d:\s+Starting items: (?P<items>.*)\s+"
               r"Operation: new = (?P<operation>.+)\s+"
               r"Test: divisible by (?P<t_divide>\d+)\s+"
               r"If true: throw to monkey (?P<t_true>\d)"
               r"\s+If false: throw to monkey (?P<t_false>\d)")
monkeys = [m.groupdict() for m in r.finditer(data)]

monkeys = [{'items': list(map(int, m['items'].split(', '))),
            'operation': m['operation'],
            't_divide': int(m['t_divide']),
            't_true': int(m['t_true']),
            't_false': int(m['t_false'])} for m in monkeys]

inspected = [0 for _ in monkeys]

# only look at the remainder of the common denominator of all the dividers
shrinker = 1
for m in monkeys:
    shrinker *= m['t_divide']

# rounds
for r in range(10000):

    for m_idx, m in enumerate(monkeys):

        for item in m['items']:

            # inspect
            old = item
            item = eval(m['operation'])
            # item = item // 3
            item = item % shrinker

            if item % m['t_divide'] == 0:
                monkeys[m['t_true']]['items'].append(item)
            else:
                monkeys[m['t_false']]['items'].append(item)

            m['items'] = m['items'][1:]
            inspected[m_idx] += 1

    if r % 1000 == 0:
        print(f"Round {r}/10000")

    # print(f"\nAfter round {r}\n===============")
    # for m_idx, m in enumerate(monkeys):
    #    print(f"Monkey {m_idx} has items {m['items']}")


print(f"Answer 2: {sorted(inspected)[-2] * sorted(inspected)[-1]}")
