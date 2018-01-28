tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'mouse', 'goose']
]


def printTable(tableData):
    for i in range(len(tableData)):
        maxColWidth = 0
        for j in range(len(tableData[i])):
            if (len(tableData[i][j]) > maxColWidth):
                maxColWidth = len(tableData[i][j])
        for k in range(len(tableData[i])):
            tableData[i][k] = tableData[i][k].rjust(maxColWidth)
    for x in range(4):
        for y in range(3):
            if (y < 2):
                print(tableData[y][x], end=' ')
            else:
                print(tableData[y][x])


printTable(tableData)
