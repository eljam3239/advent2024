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

   #print(sum)

    pattern2 = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    valid_instructions2 = []
    valid_instructions2 = re.findall(pattern2, instructions)
    enabled = True
    sum = 0
    for instruction in valid_instructions2:
        match instruction[0]:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                if enabled:
                    product = int(instruction[1]) * int(instruction[2])
                    sum+=product
    print(sum)
    