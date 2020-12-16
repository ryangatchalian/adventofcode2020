inputs = [list(line) for line in open('day11-input.txt', 'r').read().split('\n')]


def p1check_neighbors(row: int, col: int, input_list: list) -> int:
    sides = (-1, 0, 1)
    occupied = 0
    row_bound = len(input_list)
    col_bound = len(input_list[0])
    for diff_row in sides:
        current_row = row + diff_row
        if 0 <= current_row < row_bound:
            for diff_col in sides:
                current_col = col + diff_col
                if 0 <= current_col < col_bound:
                    if (current_row, current_col) != (row, col) and input_list[current_row][current_col] == '#':
                        occupied += 1
    return occupied


def p2check_neighbors(row: int, col: int, input_list: list) -> int:
    sides = (-1, 0, 1)
    occupied = 0
    row_bound = len(input_list)
    col_bound = len(input_list[0])
    for diff_row in sides:
        for diff_col in sides:
            if diff_row == diff_col == 0:
                continue
            current_col = col + diff_col
            current_row = row + diff_row
            while (
                    0 <= current_row < row_bound and 0 <= current_col < col_bound and
                    input_list[current_row][current_col] == '.'
            ):
                current_row += diff_row
                current_col += diff_col
            if (
                    0 <= current_row < row_bound and 0 <= current_col < col_bound and
                    input_list[current_row][current_col] == '#'
            ):
                occupied += 1
    return occupied


def p1solution(input_list: list, check_neighbors_func) -> int:
    while True:
        new_list = []
        for row, line in enumerate(input_list):
            new_row = []
            for col, seat in enumerate(line):
                occupied = check_neighbors_func(row, col, input_list)
                if seat == 'L' and occupied == 0:
                    new_row.append('#')
                elif seat == '#' and occupied >= 4:
                    new_row.append('L')
                else:
                    new_row.append(seat)
            new_list.append(new_row)
        if new_list == input_list:
            return sum(seat == '#' for row in new_list for seat in row)
        else:
            input_list = new_list


def p2solution(input_list: list, check_neighbors_func) -> int:
    while True:
        new_list = []
        for row, line in enumerate(input_list):
            new_row = []
            for col, seat in enumerate(line):
                occupied = check_neighbors_func(row, col, input_list)
                if seat == 'L' and occupied == 0:
                    new_row.append('#')
                elif seat == '#' and occupied >= 5:
                    new_row.append('L')
                else:
                    new_row.append(seat)
            new_list.append(new_row)
        if new_list == input_list:
            return sum(seat == '#' for row in new_list for seat in row)
        else:
            input_list = new_list


part1 = p1solution(inputs, p1check_neighbors)
part2 = p2solution(inputs, p2check_neighbors)
print(f"Part 1 Answer: {part1}")
print(f"Part 1 Answer: {part2}")