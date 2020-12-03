

def password_validation(inputlist):
    counter = 0
    for combo in inputlist:
        policy, password = combo.split(': ')
        letter = policy[::-1][0]
        minval, maxval = policy[:-2].split('-')
        if int(minval) <= password.count(letter) <= int(maxval):
            counter += 1
    return counter


def actual_pass_verification(inputlist):
    counter = 0
    for combo in inputlist:
        policy, password = combo.split(': ')
        letter = policy[::-1][0]
        pos1, pos2 = policy[:-2].split('-')
        index1 = int(pos1) - 1
        index2 = int(pos2) - 1
        if (password[index1] == letter) ^ (password[index2] == letter):
            counter += 1
    return counter

f = open("day2-input.txt", 'r')
inputs = f.read().split('\n')
inputs.remove('')

day2_answer = password_validation(inputs)
print(f"Day 2 Answer (Part 1): {day2_answer}")
day2_answer = actual_pass_verification(inputs)
print(f"Day 2 Answer (Part 1): {day2_answer}")