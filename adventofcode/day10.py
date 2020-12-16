inputs = [int(line) for line in open('day10-input.txt', 'r').read().split('\n')]
combo = [1, 1, 2]


def part1_solution(values: list) -> int:
    total_diff = {1: 0, 2:0, 3:0}

    for i, number in enumerate(values):
        if i < len(values) - 1:
            diff = values[i + 1] - number
            total_diff[diff] += 1

    return total_diff[1] * total_diff[3]


def combinations(val: int) -> int:
    global combo
    if val < len(combo):
        return combo[val]
    else:
        temp_combo = combinations(val - 1) + combinations(val - 2) + combinations(val - 3)
        combo.append(temp_combo)
        return temp_combo


def part2_solution(values: list) -> int:
    # minimum number of combinations
    ans = 1
    continuous = 0
    pointer = 0
    for number in values:
        if number == pointer + 1:
            continuous += 1
        else:
            ans *= combinations(continuous)
            continuous = 0
        pointer = number
    ans *= combinations(continuous)
    return ans


# outlet to adapter
inputs.append(0)
# highest adapter to device
inputs.append(max(inputs) + 3)
# sort list
inputs.sort()

part1 = part1_solution(inputs)
part2 = part2_solution(inputs)
print(f"Part 1 Answer: {part1}")
print(f"Part 2 Answer: {part2}")


