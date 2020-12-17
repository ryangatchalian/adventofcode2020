inputs = [line for line in open('day13-input.txt', 'r').read().splitlines()]


def p1_solution(bus_ids: list, timestamp: int):
    next_ts = 0
    bus_id = 0
    for val in bus_ids:
        b_id = int(val)
        earliest = ((timestamp // b_id) + 1) * b_id
        if next_ts == 0 or earliest < next_ts:
            next_ts = earliest
            bus_id = b_id
    return bus_id * (next_ts - timestamp)


def p2_solution(bus_ids: list):
    time = 0
    multiplier = bus_ids[0][0]
    for bus, step in bus_ids[1:]:
        while (time + step) % bus != 0:
            time += multiplier
        multiplier *= bus
    return time


timestamp = int(inputs[0])
bus_sched = [int(bus) for bus in inputs[1].split(sep=',') if bus != 'x']
print(bus_sched)

part1 = p1_solution(bus_sched, timestamp)
print(f"Part 1 Answer: {part1}")
print('')

promo_sched = [(int(bus), step) for step, bus in enumerate(inputs[1].split(sep=',')) if bus != 'x']
print(promo_sched)
part2 = p2_solution(promo_sched)
print(f"Part 2 Answer: {part2}")