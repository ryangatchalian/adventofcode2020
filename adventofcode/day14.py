inputs = [line.split(' = ') for line in open('day14-input.txt', 'r').read().split('\n')]
print(inputs)
mask = inputs[0]


def p1_solution(input_list: list):
    memory = {}
    for line in input_list:
        if 'mask' in line[0]:
            bit_mask = line[1]
        else:
            bit_val = f'{int(line[1]):036b}'

            for i in range(len(bit_val)):
                if bit_mask[i] == 'X' or bit_mask[i] == bit_val[i]:
                    continue
                else:
                    bit_val = bit_val[:i] + bit_mask[i] + bit_val[i+1:]
            memory[line[0].strip('me[]')] = int(str(bit_val),2)
    return sum(memory.values())


def get_addresses(address: str):
    if 'X' not in address:
        return address
    else:
        output = ''
        x_index = address.index('X')
        address0 = address[:x_index] + '0' + address[x_index + 1:]
        address1 = address[:x_index] + '1' + address[x_index + 1:]
        output += get_addresses(address0) + ',' + get_addresses(address1)
        return output


def p2_solution(input_list: list):
    memory = {}
    for line in input_list:
        if 'mask' in line[0]:
            bit_mask = line[1]
        else:
            bit_val = f"{int(line[0].strip('me[]')):036b}"
            for i in range(len(bit_val)):
                if bit_mask[i] == bit_val[i]:
                    continue
                elif bit_mask[i] == 'X':
                    bit_val = bit_val[:i] + bit_mask[i] + bit_val[i+1:]
                else:
                    new_val = int(bit_mask[i]) | int(bit_val[i])
                    bit_val = bit_val[:i] + str(new_val) + bit_val[i+1:]

            address_list = get_addresses(bit_val).split(',')
            for address in address_list:
                memory[int(address, 2)] = int(line[1])
    return sum(memory.values())


part1 = p1_solution(inputs)
print(f"Part 1 Answer: {part1}")
part2 = p2_solution(inputs)
print(f"Part 2 Answer: {part2}")
