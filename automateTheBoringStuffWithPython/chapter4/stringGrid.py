grid = [['.','.','.','.','.','.'],
        ['.','o','o','.','.','.'],
        ['o','o','o','o','.','.'],
        ['o','o','o','o','o','.'],
        ['.','o','o','o','o','o'],
        ['o','o','o','o','o','.'],
        ['o','o','o','o','.','.'],
        ['.','o','o','.','.','.'],
        ['.','.','.','.','.','.'],
        ]

newGrid = [['.','.','.','.','.','.', '.', '.', '.'],
           ['.','.','.','.','.','.', '.', '.', '.'],
           ['.','.','.','.','.','.', '.', '.', '.'],
           ['.','.','.','.','.','.', '.', '.', '.'],
           ['.','.','.','.','.','.', '.', '.', '.'],
           ['.','.','.','.','.','.', '.', '.', '.']]

x = 0
while(x < len(grid)):
    y = 0
    innerLen = len(grid[x])
    while(y < innerLen):
        newGrid[y][x] = grid[x][y]
        y = y + 1
    x = x + 1

i = 0
while(i < len(newGrid)):
    j = 0
    innerLen = len(newGrid[i])
    while(j < innerLen):
        if(j == innerLen - 1):
            print(newGrid[i][j])
        else:
            print(newGrid[i][j], end='')
        j = j + 1
    i = i + 1