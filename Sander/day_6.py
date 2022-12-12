########################################################################################################################
def script(path_input):
    with open(path_input, 'r') as input_file:
        input = input_file.read().splitlines()

    # Part 1 & 2 #######################################################################################################
    marker = []
    marker_length = 0
    count = 0
    detect_marker = True

    for c in list(input[0]):
        count += 1
        if c in marker:
            marker_length -= marker.index(c) + 1
            marker = marker[marker.index(c) + 1:]
        marker_length += 1
        marker += [c]

        if detect_marker and len(marker) == 4:
            detect_marker = False
            print(f'Solution part 1: {count}')
        elif len(marker) == 14:
            print(f'Solution part 2: {count}')
            break


########################################################################################################################
if __name__ == "__main__":
    script(path_input=f'../input/day_{__file__.split(".")[0][-1]}.txt')
