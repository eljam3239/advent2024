def parse_input(input_data):
    rules_section, updates_section = input_data.split('\n\n')
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
    return rules, updates

def is_update_correct(update, rules):
    page_positions = {page: i for i, page in enumerate(update)}

    for x,y in rules:
        if x in page_positions and y in page_positions:
            if page_positions[x] >= page_positions[y]:
                return False
    return True

def calculate_middle_sum(input_data):
    rules, updates = parse_input(input_data)
    middle_sum = 0
    for update in updates:
        if is_update_correct(update, rules):
            middle_sum += update[len(update)//2]

    return middle_sum

input_data = open('day5input.txt').read().strip()
result = calculate_middle_sum(input_data)
print(result)