def leftMostColumnWithOne(binaryMatrix):
    rows, cols = binaryMatrix.dimensions()
    #rightmost corner and apply binsearch
    row, col = 0, cols - 1
    leftmost_col = -1

    while row < rows and col >= 0:
        if binaryMatrix.get(row, col) == 1:
            leftmost_col = col
            col -= 1
        else:
            row += 1

    return leftmost_col