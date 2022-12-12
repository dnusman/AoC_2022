import pandas as pd

########################################################################################################################
path_input=f'../input/day_{__file__.split(".")[0][-1]}.txt'
input = pd.read_csv(path_input, header=None, dtype=str)
input = input.iloc[:, 0].str.split('', expand=True).iloc[:, 1:-1]
input = input.apply(pd.to_numeric)

visible = pd.DataFrame(True, index=input.index, columns=input.columns)
scenic_score = pd.DataFrame(index=input.index, columns=input.columns)

for i in range(input.shape[0] - 2):
    i += 1
    for j in range(input.shape[1] - 2):
        j += 1

        tree = input.iloc[i, j]
        trees_top = input.iloc[:i, j][::-1]
        trees_bottom = input.iloc[i + 1:, j]
        trees_right = input.iloc[i, j + 1:]
        trees_left = input.iloc[i, :j][::-1]

        # Part 1
        visible_top = all(tree > trees_top)
        visible_bottom = all(tree > trees_bottom)
        visible_right = all(tree > trees_right)
        visible_left = all(tree > trees_left)

        visible.iloc[i, j] = any([visible_top, visible_bottom, visible_right, visible_left])

        # Part 2
        distance_top = len(trees_top) if visible_top else list((trees_top - tree) < 0).index(0) + 1
        distance_bottom = len(trees_bottom) if visible_bottom else list((trees_bottom - tree) < 0).index(0) + 1
        distance_right = len(trees_right) if visible_right else list((trees_right - tree) < 0).index(0) + 1
        distance_left = len(trees_left) if visible_left else list((trees_left - tree) < 0).index(0) + 1

        scenic_score.iloc[i, j] = distance_top * distance_bottom * distance_right * distance_left

print(f'Solution part 1: {visible.sum().sum()}')
print(f'Solution part 2: {scenic_score.max().max()}')