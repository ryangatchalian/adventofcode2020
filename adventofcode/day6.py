inputs = [line.strip().replace('\n',' ') for line in open("day6-input.txt").read().split('\n\n')]

part1 = 0
part2 = 0
part2_list = []
for answered_questions in inputs:
    part1 += len(set(answered_questions.replace(' ', '')))
    group = answered_questions.split()
    firstperson = set(group[0])
    for person in group:
        firstperson = firstperson.intersection(set(person))
    part2 += len(firstperson)

print(f'Part 1 Answer: {part1}')
print(f'Part 2 Answer: {part2}')