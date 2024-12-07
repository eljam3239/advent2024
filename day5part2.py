from collections import defaultdict, deque

def parse_input(input_data):
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
    return rules, updates

def is_update_correct(update, rules):
    # Map page numbers to their indices in the update
    page_positions = {page: i for i, page in enumerate(update)}
    
    # Check all relevant rules
    for x, y in rules:
        if x in page_positions and y in page_positions:
            if page_positions[x] >= page_positions[y]:
                return False
    return True

def topological_sort(pages, rules):
    # Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    # Perform topological sort
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages

def calculate_middle_sum(input_data, part_two=False):
    rules, updates = parse_input(input_data)
    middle_sum = 0
    
    for update in updates:
        if is_update_correct(update, rules):
            if not part_two:
                middle_sum += update[len(update) // 2]
        else:
            if part_two:
                # Reorder the update
                ordered_update = topological_sort(update, rules)
                middle_sum += ordered_update[len(ordered_update) // 2]
    
    return middle_sum

# Example input
input_data = open('day5input.txt').read().strip()

# Part Two calculation
result_part_two = calculate_middle_sum(input_data, part_two=True)
print(f"Sum of middle page numbers for reordered updates: {result_part_two}")
