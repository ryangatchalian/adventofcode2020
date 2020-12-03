
def count_trees(fin, right_count, down_count):
    inputfile = open(fin, "r")
    tree_count = 0
    i = 0
    row_counter = 0
    # get each line
    for line in map(str.strip, inputfile.readlines()):
        # check to see if we should look at this line
        if row_counter % down_count == 0:
            # increment if tree found
            if line[i] == "#":
                tree_count += 1
            # set index. Note that this can run beyond length of line, so use mod.
            i = (i + right_count) % len(line)
        row_counter += 1
    inputfile.close()
    return tree_count


part1_trees = count_trees("day3-input.txt", 3, 1)
print(f"Day 3 Answer (Part 1): {part1_trees}")
part2_r1d1 = count_trees("day3-input.txt", 1, 1)
part2_r3d1 = count_trees("day3-input.txt", 3, 1)
part2_r5d1 = count_trees("day3-input.txt", 5, 1)
part2_r7d1 = count_trees("day3-input.txt", 7, 1)
part2_r1d2 = count_trees("day3-input.txt", 1, 2)
print(f"r1d1: {part2_r1d1} \nr3d1: {part2_r3d1} \nr5d1: {part2_r5d1}\nr7d1: {part2_r7d1}\nr1d2: {part2_r1d2}")
print(f"Day 3 Answer (Part 2): {part2_r1d1 * part2_r3d1 * part2_r5d1 * part2_r7d1 * part2_r1d2}")


