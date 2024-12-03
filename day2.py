def is_ascending_or_decreasing(row):
    if all(row[i] < row[i + 1] for i in range(len(row) - 1)):
        return True  # Strictly ascending
    if all(row[i] > row[i + 1] for i in range(len(row) - 1)):
        return True  # Strictly descending
    return False

def legal_adjacent_diff(row):
    #any two adjacent numbers differ by at least one and at most three
    for i in range(len(row) - 1):
        if abs(row[i] - row[i + 1]) > 3 or abs(row[i] - row[i + 1]) < 1:
            return False
    return True

def solution(data):
    safe_reports = 0
    for row in data:
        if is_ascending_or_decreasing(row) and legal_adjacent_diff(row):
            safe_reports += 1
        else:
            for i in range(len(row)):
                row2 = row[:i]+row[i+1:]
                if is_ascending_or_decreasing(row2) and legal_adjacent_diff(row2):
                    safe_reports += 1
                    break
    return safe_reports

if __name__ == "__main__":
    data = []
    with open("day2input.txt", 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            data.append(row)
            #print(row)
    print(solution(data))