def printDiagonal(lst):
    print('Diagonal 1 - ' , end=" ")
    print([r[i] for i, r in enumerate(lst)])
    print('Diagonal 2 - ' , end=" ")
    print([r[~i] for i, r in enumerate(lst)])
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
printDiagonal(lst)



