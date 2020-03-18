# Author : Tri10
# NOTE   : Spaghetti Code ahead !


import csv,random
class Bollywood(object):
    """docstring for Bollywood. \n Use 'Start_game' function to play !"""

    def __init__(self):
        #initializing game variables
        self.clr()
        print('$ *-* Welcome to Bollywood game *-* $')
        self.movies_names = []
        self.turn = '#'*9
        with open('src/bollywoodmovies.csv','r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.movies_names.append(row[0])
        self.win = False

    @staticmethod
    def clr():
        print('\n'*50)
    def Start_game(self):
        #Main Start Function
        self.randommovie = ''.join(list(filter(lambda x:True if x==' ' else x.isalnum(),random.choice(self.movies_names))))
        self.board = '_' * len(self.randommovie)
        self.update(self.randommovie,self.board)
        # print('Movie name :',self.randommovie)
        i = len(self.turn)
        print("\n[/] Board => "+self.board)
        while i > 0:
            print('[/] Chances ::> '+'['+self.turn+']'+'\n')
            user = input('[?] Guess [a-z] :').lower()
            if len(user) > 1:
                print('[!] Only one alphabet !')
                continue

            elif user in self.board:
                print('[!] Already Exists !')
                continue
            else:
                if user in self.randommovie.lower():
                    print('[+] Right Guess !')

                    self.update(self.randommovie,self.board,user)
                else:
                    print('[-] Wrong !')

                    i -=1
                    self.turn = self.turn[:(len(self.turn)-1)]
            print("\n[/] Board => "+self.board)
            if self.board == self.randommovie.lower():
                print('\n @-@ OOOO Mi god ,You really win ! :......: !\n')
                break

        else:
            print("\n [*] Right Answer ==> ",self.randommovie)
            print(' :(  You Loose, Try Again  :8 ')



    def update(self,name,board,alphabet=None):
        #Updating
        board =  list(board)
        index =-1
        if alphabet:
            for i in range(name.lower().count(alphabet)):
                index = name.lower().find(alphabet,index+1)

                board[index] = alphabet

        else:
            for i in name:


                if i.lower() in ['a','e','i','o','u'] or i == ' ':



                    index = name.find(i,index+1)


                    board[index] = i.lower()

        self.board = ''.join(board)


def main():
    #Test run
    game = Bollywood()
    game.Start_game()


if __name__ == '__main__':
    main()
