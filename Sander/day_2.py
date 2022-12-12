import pandas as pd


########################################################################################################################
def script(path_input):
    input = pd.read_csv(path_input, delimiter=' ', header=None, names=['opponent', 'me'])

    # Part 1 ###########################################################################################################
    win_loss_scores = {
        ('A', 'X'): 3,
        ('B', 'X'): 0,
        ('C', 'X'): 6,
        ('A', 'Y'): 6,
        ('B', 'Y'): 3,
        ('C', 'Y'): 0,
        ('A', 'Z'): 0,
        ('B', 'Z'): 6,
        ('C', 'Z'): 3
    }

    shape_scores = {'X': 1, 'Y': 2, 'Z': 3}

    score_part_1 = input.copy()
    score_part_1[['match', 'shape']] = score_part_1.apply(lambda x: [win_loss_scores[tuple(x)], shape_scores[x['me']]],
                                                          axis=1, result_type='expand')

    total_score_part_1 = score_part_1[['match', 'shape']].sum().sum()

    print(f'Solution part 1: {total_score_part_1}')

    # Part 2 ###########################################################################################################
    score_part_2 = input.copy()
    action = {
        ('A', 'X'): 'Z',
        ('B', 'X'): 'X',
        ('C', 'X'): 'Y',
        ('A', 'Y'): 'X',
        ('B', 'Y'): 'Y',
        ('C', 'Y'): 'Z',
        ('A', 'Z'): 'Y',
        ('B', 'Z'): 'Z',
        ('C', 'Z'): 'X'
    }

    score_part_2['action'] = score_part_2.apply(lambda x: action[tuple(x)], axis=1)
    score_part_2[['match', 'shape']] = \
        score_part_2.apply(lambda x: [win_loss_scores[tuple([x['opponent'], x['action']])], shape_scores[x['action']]],
                           axis=1, result_type='expand')

    total_score_part_2 = score_part_2[['match', 'shape']].sum().sum()

    print(f'Solution part 2: {total_score_part_2}')


########################################################################################################################
if __name__ == "__main__":
    script(path_input=f'../input/day_{__file__.split(".")[0][-1]}.txt')
