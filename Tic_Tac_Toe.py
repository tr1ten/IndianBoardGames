# Author : Tri10
# NOTE   : Spaghetti Code ahead !


import random


class  Tic_tac(object):
    """docstring for Tic_tac \n Use 'Start_game' function to play game """

    def __init__(self):
        #Setting the game variables
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.gameover = False
        self.bad = ['Nice but im better than you','You r so easy','Later Bruh ! ','HAHA We rule you one day ','AI gonna rule over world']
        self.good = ['OK Boomer','Dont get cocky Human !','Ara Ara Human-Kun','God is with you Today','OK ~~ ','Just Die Already']
        self.medium = ['I will not loose to you filthy Human ','I am going easy on you ','Just Loose already','You disgust me ']

    @staticmethod
    def clrscr():
        #Alternative for clear

        print ("\n" * 50)

    def Start_game(self):
        #Main game method , run till gameover is False
        self.clrscr()
        self.display_board()
        while not self.gameover and not self._isboardfull(self.board):



            self._playerturn()
            if self._isboardfull(self.board):
                continue
            if self.checkwin(self.board,'X'):
                self.display_board()

                print(' \n @_@ Hurray You Win ! ~~ \n ')
                break
            self.compturn()
            if self.checkwin(self.board,'O'):
                self.display_board()

                print('\n =( You Loose , Better Luck next time ! :6 \n')
                break

            self.display_board()
        else:
            print(' \n*( Uhh its a Draw !\n')

    def checkwin(self,board,marker):
        #Main Checking function if win or not
        for i in range(3):
            if board[0][i]== board[1][i] == board[2][i]==marker:

                return True

        for i in range(3):
            if board[i][0]==board[i][1] == board[i][2]==marker:

                return True

        if board[0][0]==board[1][1] == board[2][2]==marker:

            return True
        elif board[0][2]==board[1][1] == board[2][0]==marker:

            return True
        else:
            return False

    def compturn(self):
        #Trying to get best position for computer to turn
        Tboard = self.board[:]
        good_move_1 = None
        good_move_2 = None
        available_places = []
        print('Computer : ',end='')
        for positions in range(1,10):

            if self._isempty(Tboard,positions):
                # print('position :',positions)
                available_places.append(positions)
                # print('idk why tries :',positions,'Computer Board ')

                self._placeit(Tboard,positions,'O')
                best = self.checkwin(Tboard,'O')
                # self.display_board(Tboard)
                if not best:
                    self._removeit_(Tboard,positions)

                else:
                    # print('idk why its winning :',positions)
                    good_move_1 = positions
                    break
                self._placeit(Tboard,positions,'X')
                best_2 = self.checkwin(Tboard,'X')
                if not best_2:

                    self._removeit_(Tboard,positions)
                    continue
                else:
                    # print('idk why users winning :',positions)
                    good_move_2 = positions
                    self._removeit_(Tboard,positions)
        else:
            if good_move_2 is None:
                print(f' "{random.choice(self.good)} !"')
                good_move_2 = random.choice(available_places)
            else:
                print(f' "{random.choice(self.medium)} !"')
            self._placeit(self.board,good_move_2,'O')
            return 0
        print(f' "{random.choice(self.bad)} !"')

        self._placeit(self.board,good_move_1,'O')



    def _removeit_(self,board,position):
        coords = self._getcoords(position)
        board[coords[0]][coords[1]] = ' '
    def display_board(self,board=None):
        if board is None:
            board = self.board

        #displaying board on console
        print('Board :> \n\n')
        print(f' {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  ')
        print('____ _____ ____')
        print()
        print(f' {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  ')
        print('____ _____ ____')
        print()
        print(f' {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  ')
        print()

    def  _playerturn(self):

        #Asking for user choice and placing it on Board
        while 1 and not self._isboardfull(self.board):
            try:
                position = int(input('Place "X" on Board at ? (1 to 9) :'))
            except Exception:
                print('Only Numbers Allowed !')
            else:
                if position <=9 and position>0:
                    if not self._isempty(self.board,position):
                        print("Space Already Aquired !")
                        continue
                    else:

                        self._placeit(self.board,position,'X')
                        break
                else:
                    print('Expected input range- 1 to 9 , got {}'.format(position))
    def _isboardfull(self,board):
        #Checking if board full or not
        for row in board:
            for  column in row:
                if column == ' ':

                    return False
        else:
            return True
    def _placeit(self,board,position,marker):
        coords = self._getcoords(position)
        #Just Modifying the Board
        board[coords[0]][coords[1]] = marker
    def _getcoords(self,position):
        #getting position for 2d array
        if position <=3:
            return [0,position-1]
        elif position<=6:
            return [1,(position-3)-1]
        elif position <=9:
            return [2,(position-6)-1]
        else:
            return False
    def _isempty(self,board,position):
        #Checking if that position is fill or not
        coords = self._getcoords(position)
        if board[coords[0]][coords[1]] == ' ':
            return True
        else:
            return False

def main():
    #Test run
    game = Tic_tac()
    game.Start_game()


if __name__ == '__main__':
    main()
