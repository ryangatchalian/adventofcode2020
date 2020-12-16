inputs = [line for line in open("day12-input.txt", "r").read().splitlines()]

LR_directions = {
    "EL": "NWSE",
    "ER": "SWNE",
    "SL": "ENWS",
    "SR": "WNES",
    "WL": "SENW",
    "WR": "NESW",
    "NL": "WSEN",
    "NR": "ESWN"
}


def change_face(current: str, direction: str, degree: int):
    turn = current + direction
    rotations = degree // 90 - 1
    return LR_directions[turn][rotations]


def move(position: list, instruction: str):
    direction = instruction[0]
    distance = int(instruction[1:])
    if direction == "N":
        position[0] += distance
    elif direction == "S":
        position[0] -= distance
    elif direction == "E":
        position[1] += distance
    else:
        position[1] -= distance


def rotate_waypoint(wp: list, degree: int, instruction: str):
    rotations = degree // 90
    if rotations % 4 == 1:
        wp = wp[1:] + wp[:1]
        if instruction[0] == "R":
            wp[0] *= -1
        else:
            wp[1] *= -1
    elif rotations % 4 == 2:
        wp[0] *= -1
        wp[1] *= -1
    elif rotations % 4 == 3:
        wp = wp[1:] + wp[:1]
        if instruction[0] == "R":
            wp[1] *= -1
        else:
            wp[0] *= -1
    return wp


def move2waypoint(position: list, wp: list, instruction: str):
    multiplier = int(instruction[1:])
    waypoint_x = abs(wp[0])
    waypoint_y = abs(wp[1])
    if wp[0] < 0:
        position[0] -= (waypoint_x * multiplier)
    else:
        position[0] += (waypoint_x * multiplier)
    if wp[1] < 0:
        position[1] -= (waypoint_y * multiplier)
    else:
        position[1] += (waypoint_y * multiplier)


def p1_solution(input_list: list, position: list):
    for instruction in input_list:
        if instruction[0] == "F":
            new_instruct = position[2] + instruction[1:]
            move(position, new_instruct)
        elif instruction[0] == "L" or instruction[0] == "R":
            degree = int(instruction[1:])
            position[2] = change_face(position[2], instruction[0], degree)
        else:
            move(position, instruction)
    return abs(position[0]) + abs(position[1])


def p2_solution(input_list: list, position: list, wp: list):
    for instruction in input_list:
        if instruction[0] == "F":
            move2waypoint(position, wp, instruction)
        elif instruction[0] == "L" or instruction[0] == "R":
            degree = int(instruction[1:])
            wp = rotate_waypoint(wp, degree, instruction)
        else:
            move(wp, instruction)
    return abs(position[0]) + abs(position[1])


ship = [0, 0, "E"]
part1 = p1_solution(inputs, ship)
print(f"Part 1 Answer: {part1}")

ship2 = [0, 0, "E"]
waypoint = [1, 10]
part2 = p2_solution(inputs, ship2, waypoint)
print(f"Part 1 Answer: {part2}")