from collections import defaultdict
import re

inputs = open("day16-input.txt", "r").read()
# print(inputs)

rules_list = re.compile(r'^([^>:]+): (\d+)-(\d+) or (\d+)-(\d+)$')


def ticket_parsing(tickets: str):
    return [int(x) for x in tickets.split(',')]


def data_parsing(input_list: str):
    fields, your_ticket, nearby_tickets = input_list.split('\n\n')
    rules = {}
    for line in fields.splitlines():
        match = rules_list.match(line)
        assert match is not None, line
        rules[match[1]] = (int(match[2]), int(match[3]), int(match[4]), int(match[5]))

    my_ticket = ticket_parsing(your_ticket.splitlines()[1])

    ticket_lines = nearby_tickets.splitlines()
    nearbytix = [ticket_parsing(line) for line in ticket_lines[1:]]

    return rules, my_ticket, nearbytix


def p1_solution(rules: dict, ticket_list: list):
    output = 0
    for ticket in ticket_list:
        for number in ticket:
            for l1, l2, u1, u2 in rules.values():
                if l1 <= number <= l2 or u1 <= number <= u2:
                    break
            else:
                output += number
    return output


def p2_solution(rules: dict, my_ticket: list, tickets:list):
    valid = []
    for ticket in tickets:
        if all(
            any(
                l1 <= number <= l2 or u1 <= number <= u2
                for l1, l2, u1, u2 in rules.values()
            )
            for number in ticket
        ):
            valid.append(ticket)

    possible_pos = defaultdict(set)
    for pos in range(len(valid[0])):
        for key, (l1, l2, u1, u2) in rules.items():
            for ticket in valid:
                if not (l1 <= ticket[pos] <= l2 or u1 <= ticket[pos] <= u2):
                    break
            else:
                possible_pos[pos].add(key)

    positions = {}
    while possible_pos:
        for key, value in tuple(possible_pos.items()):
            if len(value) == 1:
                k, = value
                positions[k] = key
                possible_pos.pop(key)
                for v in possible_pos.values():
                    v.discard(k)

    ret = 1
    for key, value in positions.items():
        if key.startswith('departure '):
            ret *= my_ticket[value]

    return ret





rules, mytix, nearbytix = data_parsing(inputs)

part1 = p1_solution(rules, nearbytix)
print(f"Part 1 Answer: {part1}")

part2 = p2_solution(rules, mytix, nearbytix)
print(f"Part 2 Answer: {part2}")