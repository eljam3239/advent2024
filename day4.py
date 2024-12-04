def is_horizontal_right(data, x, y):
    if x<= len(data[i]) and data[x+1][y] == 'M' and data[x+2][y] == 'A' and data[x+3][y] == 'S':
        return True
def is_horizontal_left(x, y):
    if x>=3 and data[x-1][y] == 'M' and data[x-2][y] == 'A' and data[x-3][y] == 'S':
        return True

def is_vertical(x, y):
    pass

def is_diagonal(x, y):
    pass


if __name__ == '__main__':
    #read in day4input.txt as 2d array
    with open('day4input.txt', 'r') as file:
        data = [list(line.strip()) for line in file]
#print(data[0][0])
    xmas_count = 0
    for i in range(len(data)):
        for j in range(len(data[i])-3):
            if data[i][j] == 'X':
                if data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
                    xmas_count += 1
    print(xmas_count)
        