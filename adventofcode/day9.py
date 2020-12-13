inputs = [int(line.strip().replace('\n', ' ')) for line in open('day9-input.txt', 'r').read().split('\n')]


def two_sum(value_list: list, target: int):
    sums_dict = {}
    for value in value_list:
        diff = target - value
        if diff in sums_dict:
            return True
        else:
            sums_dict[value] = diff
    return False


def encryption(value_list: list, target_ind: int):
    lo = target_ind - 1
    high = target_ind
    target = value_list[target_ind]
    lowest_possible = 0
    while lo < high:
        list_sum = sum(value_list[lo:high])
        if lo == lowest_possible and list_sum > target:
            high -= 1
        elif lo == lowest_possible and list_sum < target:
            high += 1
            lo += 1
            lowest_possible += 1
        elif list_sum > target:
            lo -= 1
        else:
            return min(value_list[lo:high]) + max(value_list[lo:high])


start = 0
end = preamble = 25

for i in range(len(inputs) - 1):
    target_val = inputs[i + preamble]
    target_list = inputs[start:end]
    if not two_sum(target_list, target_val):
        print(f"Part 1 Answer: {target_val}")
        target_index = i + preamble
        break
    start += 1
    end += 1

part2 = encryption(inputs, target_index)
print(f"Part 2 Answer: {part2}")