'''
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

Rules for validation

    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

    no numpy import

'''

import types

class Sudoku(object):
    def __init__(self, data):
        '''
        Initiate Sudoku class.

        Input: any 2D matrix.
        '''

        self.data = data

    

    def is_valid(self) -> bool:
        '''
        Validates the sudoku matrix.


        Returns
        ---------
        True if valid according to rules, otherwise False.
        
        '''

        N = len(self.data)

        if N != len(self.data[0]): # check if square
            print('Not square')
            return False

        if N == 1: # if 1x1
            unique_value= self.data[0][0]
            
            if type(unique_value) != type(1): # check if integer
                print('Not an integer')
                return False
            
            return True if unique_value == 1 else False # only "1" can be a valid solution
        
        # check row- and col-wise and element validity
        for m in range(N):
            col = []
            for n, row in enumerate(self.data):
                if len(set(row)) < len(row):
                    print(f'Duplicate in row {n+1}')
                    return False

                curr_value = self.data[n][m]
                
                if type(curr_value) != type(1): # ckeck if int and not bool
                    print(f'Invalid character in position [{n+1}, {m+1}]')
                    return False

                if not 1 <= curr_value <= N:
                    print('Found number outside valid range')
                    return False
                
                col.append(curr_value)
            
            if len(set(col)) < n: # checks for duplicates column-wise
                print(f'Duplicate in column {m+1}')
                return False
        
        # check squares
        square_size = 0

        for n in range(1, N): # calculate square size
            if N//n == n:
                square_size = n

        if square_size == 0:
            print('Empty matrix')
            return False
        
        
        squares = [[self.data[horiz*square_size+xh][vert*square_size+xv]
                        for m, horiz in enumerate(range(square_size))
                        for n, vert in enumerate(range(square_size))
                        for xh in range(square_size)
                        for xv in range(square_size)]]
#                        curr_square.append(self.data[horiz*square_size+xh][vert*square_size+xv])

        for square in squares:
            if len(set(square)) < N:
                print(f'Duplicate in square [{n+1}, {m+1}]')
                return False

        print("Valid Sudoku!")        
        return True



if __name__ == '__main__':

    valid_matrix = [
        [7,8,4,  1,5,9,  3,2,6],
        [5,3,9,  6,7,2,  8,4,1],
        [6,1,2,  4,3,8,  7,5,9],

        [9,2,8,  7,1,5,  4,6,3],
        [3,5,7,  8,4,6,  1,9,2],
        [4,6,1,  9,2,3,  5,8,7],

        [8,7,6,  3,9,4,  2,1,5],
        [2,4,3,  5,6,1,  9,7,8],
        [1,9,5,  2,8,7,  6,3,4]
            ]

    invalid_matrix = [
        [7,8,4,  1,5,9,  3,2,6],
        [5,3,9,  6,7,2,  8,4,1],
        [6,1,2,  4,2,8,  7,5,9],

        [9,2,8,  7,1,5,  4,6,3],
        [3,5,7,  8,4,6,  1,9,2],
        [4,6,1,  9,2,3,  5,8,7],

        [8,7,6,  3,9,4,  2,1,5],
        [2,4,3,  5,6,1,  9,7,8],
        [1,9,5,  2,8,7,  6,3,4]
            ]

    # Invalid Sudoku
    badSudoku1 = [
        [0,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
        
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
        
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9],
        [1,2,3, 4,5,6, 7,8,9]
        ]

    badSudoku2 = [
        [1,2,3,4,5],
        [1,2,3,4],
        [1,2,3,4],  
        [1]
    ]


    matrices = [valid_matrix, invalid_matrix, badSudoku1, badSudoku2]

    for matrix in matrices:
        print(Sudoku(matrix).is_valid())