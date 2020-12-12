inputs = [line.strip().replace('.\n','') for line in open("day7-input.txt").read().split('\n')]
# inputs = [line.strip().replace('.\n','') for line in open("test-input.txt").read().split('\n')]


def find_parents(string, bag_dictionary, output):
    if len(string) == 0:
        return output
    else:
        parent = set()
        for searched_bag in string:
            for bag in bag_dictionary:
                if searched_bag in bag_dict[bag]:
                    parent.add(bag)
                    output.add(bag)
        return find_parents(parent, bag_dictionary, output)


def total_bags(string, bag_dictionary):
    temp_list = bag_dictionary[string].split(', ')
    total = 0
    if temp_list[0][0].isdigit():
        for combo in temp_list:
            bag_count = int(combo[0])
            templine = combo.split()
            bag_name = f"{templine[1]} {templine[2]}"
            total += bag_count + bag_count * total_bags(bag_name, bag_dictionary)
        return total
    else:
        return 0

bag_dict = {}
part1_set = set()
for bag in inputs:
    splitline = bag.split(' bags contain')
    bag_dict[f'{splitline[0]}'] = splitline[1].strip()

find_parents({"shiny gold"}, bag_dict, part1_set)

print(f"Part 1 Answer: {len(part1_set)}")
print(f"Part 2 Answer: {total_bags('shiny gold', bag_dict)}")

