inputs = [line.strip().replace('\n',' ') for line in open("day5-input.txt").read().split('\n')]

answers = []
seat_ids = set()
for boardingpass in inputs:
    totalrows = [0, 127]
    totalcolumns = [0, 7]
    for character in boardingpass:
        if character == "F":
            totalrows[1] = (totalrows[1] - ((totalrows[1] - totalrows[0]) // 2)) - 1
        elif character == "B":
            totalrows[0] = ((totalrows[1] - totalrows[0]) // 2 + 1) + totalrows[0]
        elif character == "L":
            totalcolumns[1] = (totalcolumns[1] - ((totalcolumns[1] - totalcolumns[0]) // 2)) - 1
        else:
            totalcolumns[0] = ((totalcolumns[1] - totalcolumns[0]) // 2 + 1) + totalcolumns[0]
    seat_ids.add(totalrows[0] * 8 + totalcolumns[0])

part1 = max(seat_ids)
part2 = set(range(min(seat_ids), max(seat_ids))) - seat_ids

print(f"Part 1 Answer: {part1}")
print(f"Part 2 Answer: {part2}")
