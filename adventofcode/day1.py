f = open("day1-input.txt", 'r')
inputs = f.read().split('\n')
inputs.remove('')
inputs = [int(value) for value in inputs]


def two_sum(numbers: list):
    x = set()
    target = 2020
    for value in numbers:
        difference = target - value
        if difference in x:
            return value, difference
        x.add(value)
    return "No Match."


def threeSum(numbers):
    numbers.sort()
    target = 2020
    for i, num in enumerate(numbers):
        if i > 0 and num == numbers[i - 1]:
            continue
        l,r = i+1, len(numbers) - 1
        while l < r:
            threesum = num + numbers[l] + numbers[r]
            if threesum > target:
                r -= 1
            elif threesum < target:
                l += 1
            else:
                return [num,numbers[l],numbers[r]]
    return "None found."


number1, number2 = two_sum(inputs)
print(number1, number2)
print(f'Answer: {number1 * number2}')

print('=' * 80)

part2 = threeSum(inputs)
print(part2)
print(f'Answer: {part2[0] * part2[1] * part2[2]}')