def is_mas_top_left_to_bottom_right(i, j):
    return i <= rows - 3 and j <= cols - 3 and \
        data[i][j] == 'M' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S'

def is_mas_top_right_to_bottom_left(i, j):
    return i <= rows - 3 and j >= 2 and \
        data[i][j] == 'M' and data[i+1][j-1] == 'A' and data[i+2][j-2] == 'S'

def is_mas_bottom_left_to_top_right(i, j):
    return i >= 2 and j <= cols - 3 and \
        data[i][j] == 'M' and data[i-1][j+1] == 'A' and data[i-2][j+2] == 'S'

def is_mas_bottom_right_to_top_left(i, j):
    return i >= 2 and j >= 2 and \
        data[i][j] == 'M' and data[i-1][j-1] == 'A' and data[i-2][j-2] == 'S'

if __name__ == '__main__':
    # Read in day4input.txt as 2D array
    with open('day4input.txt', 'r') as file:
        data = [list(line.strip()) for line in file]
    rows = len(data)
    cols = len(data[0])
    count = 0

    _set = {"M", "S"}

        # find A as center of the cross, then check the diagonals
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == "A":
                if {data[r - 1][c - 1], data[r + 1][c + 1]} == _set and {data[r - 1][c + 1], data[r + 1][c - 1]} == _set:
                    count += 1

    print(count)
