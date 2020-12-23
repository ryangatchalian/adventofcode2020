day15_input = [0, 1, 4, 13, 15, 12, 16]
test_input = [0, 3, 6]
turn = 0
current = 0


def solution(input_list: list, last_spoken: int):
    global turn, current
    list_length = len(input_list)
    memory = {}
    for i, number in enumerate(input_list):
        if i + 1 == list_length:
            turn = i + 1
            current = number
            break
        memory[number] = i + 1

    while turn < last_spoken:
        # print(f"Turn: {turn}, Current: {current}")
        if current not in memory.keys():
            next_val = 0
        else:
            next_val = turn - memory[current]
        memory[current] = turn
        current = next_val
        turn += 1
    # print(f"Turn: {turn}, Current: {current}")
    return current


part1 = solution(day15_input, 2020)
print(f"Part 1 Answer: {part1}")
part2 = solution(day15_input, 30000000)
print(f"Part 2 Answer: {part2}")
