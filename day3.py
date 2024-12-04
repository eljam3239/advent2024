import re

if __name__ == '__main__':
    instructions = ""
    with open("day3input.txt", 'r') as file:
        for line in file:
            instructions += line
    #print(instructions[0:5])
    pattern = r"mul\((-?\d{1,3}),\s*(-?\d{1,3})\)"
    valid_instructions = []
    sum = 0
    valid_instructions = re.findall(pattern, instructions)
    for instruction in valid_instructions:
        product = int(instruction[0]) * int(instruction[1])
        sum+=product

    print(sum)