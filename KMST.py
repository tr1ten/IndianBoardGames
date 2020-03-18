# Author : Tri10
# NOTE   : Poor Code ahead !


import random,time,sys
class KMST:
	"""docstring for KMST,  \n Use 'Start_game' function to play !"""
	def __init__(self):

		self.choices = {'Raja':1000,'Chor':0,'Mantri':800,'Sepai':500}
		self.p = ['Raja','Chor','Mantri','Sepai']
		self.totalscore = 0
		self.score = 0
		self.comp1 = 0
		self.comp2 = 0
		self.comp3 = 0
		self.Points = [0,500,800,1000]
		self.swap = False
		self.swap2 = False
		self.animation = "|/-\\"
		print('\n---: Welcome to RAJA-MANTRICHOR-SEPAI :--- \n')
	def Start_game(self):
		#Main method 
		input('[/] hit enter to play the game.. ')
		for j in range(5):
			self.swap = False
			self.swap2 =  False
			print('\n|| SCore Board of  Rounds : [{}/{}] ||'.format(j+1,5))
			print('|| Computer 1 : [{}] | Computer 2 : [{}] | Computer 3 : [{}] |'.format(self.comp1,self.comp2,self.comp3),end='')
			print('| User Score : [{}] ||\n '.format(self.totalscore))
			for i in range(20):
				time.sleep(0.1)
				sys.stdout.write("\r"+self.animation[i%len(self.animation)]+' Throwing Named Chits '+self.animation[i%len(self.animation)])
				
				sys.stdout.flush()
			
			sys.stdout.flush()
			print('\n\n[^] Deck on Table > |:| |:| |:| |:|\n')
			print('[~] You got {}'.format(self.userchoice()))
		
			if self.usrgot == 'Mantri':
				self.mantri() 
			else:
				if self.usrgot == 'Chor':
					chance = random.choice([0,800])
					if chance == 800:
						print('[+] Mantri Got it  Wrong ! You Get 800 Points')
						self.swap2 = True 
					else:
						print('[-] Mantri Got it  Right ! You Get 0 Points')
					self.score = chance
				else:	
			 		self.score = self.choices.get(self.usrgot)
			 		print('[+] You got score {}'.format(self.score))
			backup = self.p[:]
			backup.remove(self.usrgot)
			new = []
			
			for k in backup:
				# print('here is :',k)
				if k == 'Chor' and self.swap:
					new.append(800)
				elif  k == 'Mantri' and self.swap2:
					# print('swap2 is true and this is mantri ',self.swap2)
					new.append(0)
				else:
					new.append(self.choices.get(k))
			# print('Current : ',new)

			self.comp1 +=new[0]
			self.comp2 +=new[1]
			self.comp3 +=new[2]
			
			self.totalscore +=self.score
		scores = [self.comp1,self.comp2,self.comp3,self.totalscore]
		winner = scores.index(max(scores))+1
		if winner == 4:
			win = 'You'
		else:
			win = f'Computer {winner}'
		print('[//] Game Ended \n[=] Your Total Score :',self.totalscore)
		print("{} Win the Game ".format(win))
		
	def mantri(self):
		#Mantri method quite simple 
		print('[HINT] {} is the King '.format(self.p.index('Raja')+1))
		while 1:
			user = int(input('[?] Who is Thief (1to4):'))-1
			if user > 4 :
				print('Exceeded the  Excepted range !')
				continue
			if user != self.usr:break 
			else:
				print('Exclude yourself')
		if user == self.p.index('Chor'):
			print('[+] You got it right !')

			self.score =800
		else:
			print('[-] You got it Wrong ! {} is the Chor'.format(self.p.index('Chor')))
			self.swap = True
			self.score =0





	def userchoice(self):
		#Getting user choice 
		while 1:
			try:
				self.usr = int(input('[?] Pick Any of the Four Chits (1-4) :')) - 1
			except Exception :
				print('[! Only integer value allowed !')

			else:
				break
		random.shuffle(self.p)
		self.usrgot = self.p[self.usr]
		return self.usrgot


def main():
    #Test run
    game = KMST()
    game.Start_game()


if __name__ == '__main__':
    main()



