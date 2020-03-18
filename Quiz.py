import math
import time
import random
from threading import Timer
class Quiz(object):
 	"""docstring for Quiz , Use 'Start_game' method to play"""
 	def __init__(self):
 		print('-- Welcome to MaTrIx --')
 		self.level = 1
 		self.operations = ['÷','*','+','-','+','+','+','-','-'] 
 		self.gameover = False
 		self.score= 0


 	def Start_game(self):
 		i = 0
 		f = 3
 		
 		
 		while not self.gameover:
 			print(f'\n[.] Score : {self.score} | Current level {self.level}\n')
 			t = Timer(5+(self.level*f//3),print,['\n[x] Times Up !\nhit enter...'])
 			t.start()
 			ques = ''.join([f"{random.randint(1*self.level,10*self.level)}{random.choice(self.operations)}" for  i in range(f//3+1)])[:-1]
 			print(f'[=] Time Limit : {5+(self.level*f//3)} secs \n[?] Question -> {ques}')
 			ans = (input('[/] Ans :'))

 			t.cancel()
 			if ans:
 				try:
 					ans = int(ans)
 				except Exception:
 					print('[!] Only Interger Allowed ! , Try Again')
 					continue
 			realans =  math.floor(eval(ques.replace('÷','/')))
 			if ans == realans:
 				self.score +=1
 				print('[+] Right Answer !')
 			else:

 				print('[-] Wrong Answer ! Correct is ',realans)
 				print('++ Game over ! \n >< Your Score | {} | '.format(self.score))
 				quit(0)
 			i +=1
 			

 			if i == 5:
 				i = 0
 				f +=1
 				print('[*] You Got onto next level !')
 				self.level +=1

 			


def main():
 	quz = Quiz()
 	quz.Start_game()

if __name__ == '__main__':
 	main()




 		