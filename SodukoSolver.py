
#AUTHOR : Triten
#By using Backtracking
class SodukoSolver():
    count = 0

    def canplace(self,board, block, row, col, pos):
        # Checking if number exist in current block or not

        for rows in board[block]:
            for cell in rows:
                if cell == pos:
                    return False
        # Checking for vertically
        if block < 3:
            high = 3
            low = 0
        elif block < 6:
            high = 6
            low = 3
        elif block < 9:
            high = 9
            low = 6
        for blocks in range(low, high):

            if pos in board[blocks][row]:
                return False

        # checking horizontally
        if block in [0, 3, 6]:
            ran = [0, 3, 6]
        elif block in [1, 4, 7]:
            ran = [1, 4, 7]
        elif block in [2, 5, 8]:
            ran = [2, 5, 8]
        for blocks in (ran):
            c = list(zip(*board[blocks]))[col]
            if pos in c:
                return False
        return True


    def solveSoduko(self,board,row,cell, block):
        global count
        count +=1
        #if given cell exceeds 3 then make it 0 and row + 1

        if cell == 3:
            cell = 0
            row +=1
        #  row exceeds 3 then make it 0 and move to next block
        if row == 3:
            cell = 0
            row = 0
            block +=1

        if block == 9:
            print('\n[+] Solved in {} Tries !\n'.format(count))
            display(board)



            return True
        else:
            # print('Current block :',block,'Current loc :',(row,cell))

            if board[block][row][cell] != 0:
                return solveSoduko(board,row,cell+1,block)
            #Trying all possibilities
            for poss in range(10):
                #if it cant be place in cell then continue to next possible value
                if not canplace(board,block,row,cell,poss):
                    continue
                # puting value in cell
                board[block][row][cell] = poss
                # checking value of next cell/row/block
                np = solveSoduko(board,row,cell+1,block)
                # if placing value in next cell is pos
                if np:
                    return  True
                #if not then move to next possible value for this cell
                board[block][row][cell] = 0

            return False




    def display(self,board):
        for j in [0, 3, 6]:

            for i in zip(*board[j:3 + j]):
                print(i)


    def Start_game(self):
        print('---Welcome to Soduko Solver---')
        print('[?] enter the soduko (row by row)')
        b = [[list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))] for i in
             range(9)]
        print('Given Soduko -: \n')
        display(b)
        board = [[[0, 5, 8], [0, 0, 0], [0, 0, 2]],
                 [[2, 0, 3], [0, 0, 0], [4, 0, 5]],
                 [[1, 7, 0], [0, 0, 0], [6, 0, 8]],
                 [[8, 0, 5], [0, 0, 0], [9, 0, 7]],
                 [[3, 0, 6], [0, 0, 0], [1, 0, 2]],
                 [[7, 0, 4], [0, 0, 0], [5, 0, 6]],
                 [[0, 0, 9], [0, 0, 0], [0, 6, 1]],
                 [[5, 0, 1], [0, 0, 0], [7, 0, 9]],
                 [[2, 0, 0], [0, 0, 0], [8, 4, 0]]]
        if not solveSoduko(b, 0,0,0):
            print("Sorry Maybe Your SOduko is wrong or this program is unable to solve it !")


if __name__ == '__main__':
    SodukoSolver().Start_game()