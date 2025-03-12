import numpy as np

def print_matrix(m):
    row,col = m.shape
    for i in range(row):
        c = 1
        print('|', end='')
        for j in range(col):
            c += 1
            if(len(str(m[i][j])) == 1):
                print(' ',m[i][j], end = '  |')
                c += 6
            else:
                print(' ',m[i][j], end = ' |')
                c += 6
        print()
        print('-'*(c-col))

def walk_zigzag(floor):
    row, col = floor.shape
    for i in range(row):
        if i % 2 == 0:
            for j in range(col):
                print(floor[i, j], end=' ')
        else:
            for j in range(col-1, -1, -1):
                print(floor[i, j], end=' ')
        print()

floor1 = np.array([[ '3' , '8' , '4' , '6' , '1'],
                   ['7' , '2' , '1' , '9' , '3'],
                   ['9' , '0' , '7' , '5' , '8'],
                   ['2' , '1' , '3' , '4' , '0'],
                   ['1' , '4' , '2' , '8' , '6']]
                 )

print_matrix(floor1)
print('Walking Sequence:')
walk_zigzag(floor1)
print('################')
floor2 = np.array([[ '3' , '8' , '4' , '6' , '1'],
                   ['7' , '2' , '1' , '9' , '3'],
                   ['9' , '0' , '7' , '5' , '8'],
                   ['2' , '1' , '3' , '4' , '0']]
                 )

print_matrix(floor2)
print('Walking Sequence:')
walk_zigzag(floor2)
