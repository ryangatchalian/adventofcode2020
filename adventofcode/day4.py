import re


def requirements(single_passport):
    goal = len(single_passport)
    valid = 0
    if "byr" in single_passport and len(single_passport["byr"]) == 4 and 1920 <= int(single_passport["byr"]) <= 2002: valid += 1
    if "iyr" in single_passport and len(single_passport["iyr"]) == 4 and 2010 <= int(single_passport["iyr"]) <= 2020: valid += 1
    if "eyr" in single_passport and len(single_passport["eyr"]) == 4 and 2020 <= int(single_passport["eyr"]) <= 2030: valid += 1
    if "hgt" in single_passport and single_passport["hgt"][-2:] == "cm" and 150 <= int(single_passport["hgt"][:-2]) <= 193: valid += 1
    if "hgt" in single_passport and single_passport["hgt"][-2:] == "in" and 59 <= int(single_passport["hgt"][:-2]) <= 76: valid += 1
    if "hcl" in single_passport and re.match('^#[0-9a-f]{6}$',single_passport['hcl']): valid += 1
    if "ecl" in single_passport and re.match('^(amb|blu|brn|gry|grn|hzl|oth)$',single_passport['ecl']): valid += 1
    if "pid" in single_passport and re.match('^\d{9}$',single_passport['pid']): valid += 1
    if valid == goal:
        return True
    return False


def passport_check(single_passport, ans1, ans2):
    if len(single_passport) == 7:
        if requirements(single_passport):
            ans2 += 1
        ans1 += 1
    return ans1, ans2


inputs=[line.strip().replace('\n',' ') for line in open("day4-input.txt").read().split('\n\n')]
part1 = 0
part2 = 0
for passport in inputs:
    one_passport = {}
    # Check if blank line, meaning one whole passport was viewed
    # ans, one_passport = passport_check(one_passport, ans)
    for fields in passport.split(" "):
        field, val = fields.split(":")
        one_passport[field] = val
    one_passport["cid"] = 0
    one_passport.pop("cid")
    part1, part2 = passport_check(one_passport, part1, part2)
print(f"Part 1 Answer: {part1}\nPart 2 Answer: {part2}")
