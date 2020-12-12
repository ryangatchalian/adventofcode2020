inputs = [line.strip().replace('\n', ' ') for line in open("day8-input.txt", 'r').read().split('\n')]


def solution(input_list: list):
    i = 0
    acc_total = 0
    instruction_set = set()
    while i < len(input_list):
        command_line = input_list[i]
        command = command_line[0:3]
        if command == 'acc':
            if command_line[4] == '+':
                acc_total += int(command_line[5:])
            else:
                acc_total -= int(command_line[5:])
            i += 1
        elif command == 'jmp':
            if command_line[4] == '+':
                i += int(command_line[5:])
            else:
                i -= int(command_line[5:])
        else:
            i += 1
        if i in instruction_set:
            hasloop = True
            return hasloop, acc_total
        else:
            instruction_set.add(i)
    hasloop = False
    return hasloop, acc_total


def swapper(string: str):
    if string == "jmp":
        return "nop"
    else:
        return "jmp"


part1 = solution(inputs)
print(f"Part 1 Answer: {part1[1]}")

for index in range(len(inputs) - 1):
    current_instruction = inputs[index][0:3]
    if current_instruction != "acc":
        inputs[index] = swapper(current_instruction) + inputs[index][3:]
        loop, part2 = solution(inputs)
        if not loop:
            print(f"Part 2 Answer: {part2}")
            break
        inputs[index] = current_instruction + inputs[index][3:]

