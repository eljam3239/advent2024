def check_right_to_left(i, j):
        return j >= 3 and data[i][j] == 'X' and data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S'

def check_left_to_right(i, j):
    return j <= cols - 4 and data[i][j] == 'X' and data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S'

def check_up_to_down(i, j):
    return i <= rows - 4 and data[i][j] == 'X' and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S'
def check_down_to_up(i, j):
    return i >= 3 and data[i][j] == 'X' and data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S'

def check_diagonal_top_left_to_bottom_right(i, j):
    return i <= rows - 4 and j <= cols - 4 and \
        data[i][j] == 'X' and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S'

def check_diagonal_top_right_to_bottom_left(i, j):
    return i <= rows - 4 and j >= 3 and \
        data[i][j] == 'X' and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S'

def check_diagonal_bottom_left_to_top_right(i, j):
    return i >= 3 and j <= cols - 4 and \
        data[i][j] == 'X' and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S'

def check_diagonal_bottom_right_to_top_left(i, j):
    return i >= 3 and j >= 3 and \
        data[i][j] == 'X' and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S'


if __name__ == '__main__':
    #read in day4input.txt as 2d array
    with open('day4input.txt', 'r') as file:
        data = [list(line.strip()) for line in file]
    rows = len(data)
    cols = len(data[0])
    xmas_count = 0
    for i in range(rows):
        for j in range(cols):
            if check_left_to_right(i, j):
                xmas_count += 1
            if check_right_to_left(i, j):
                xmas_count += 1
            if check_up_to_down(i, j):
                xmas_count += 1
            if check_down_to_up(i, j):
                xmas_count += 1
            if check_diagonal_top_left_to_bottom_right(i, j):
                xmas_count += 1
            if check_diagonal_top_right_to_bottom_left(i, j):
                xmas_count += 1
            if check_diagonal_bottom_left_to_top_right(i, j):
                xmas_count += 1
            if check_diagonal_bottom_right_to_top_left(i, j):
                xmas_count += 1
    print(xmas_count)
    