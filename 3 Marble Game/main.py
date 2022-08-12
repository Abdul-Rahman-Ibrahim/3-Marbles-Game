import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image

class Game:
	width = 775
	height= 560

	possibleMoves = {
						0: [1,3,4,9],
						1: [0,2,4,9],
						2: [1,4,5,9],
						3: [0,4,6,9],
						4: [0,1,2,3,5,6,7,8,9],
						5: [2,4,8,9],
						6: [3,4,7,9],
						7: [4,6,8,9],
						8: [4,5,7,9]
	}

	#this is the position relative to canvas (not main window)
	positions = {
					0: (0,32),
					1: (width/2-8, 32),
					2: (width-13, 32),
					3: (0, height/2+20),
					4: (width/2-8, height/2+20),
					5: (width-13, height/2+20),
					6: (0, height+11),
					7: (width/2-10, height+11),
					8: (width-13, height+11)
	}

	rowWins = [
				  [0,1,2],
				  [3,4,5],
				  [6,7,8]
	]

	player1Color = 'blue'
	player2Color = 'red'

	def __init__(self):
		self.columnWins = [[self.rowWins[j][i] for j in range(len(self.rowWins[i]))] for i in range(len(self.rowWins))]
		self.leftDiagonalWins = [self.rowWins[i][i] for i in range(len(self.rowWins))]
		self.rightDiagonalWins = [self.rowWins[i][-i-1] for i in range(len(self.rowWins))]

		self.window = tk.Tk()
		self.window.geometry('780x630+100+50')
		self.window.resizable(0,0)
		self.window.title('3 Marble Game')

		self.clicked = False
		self.clickedMarblePosition = 9
		self.player1Move = True
		self.player1Win = False
		self.player2Win = False

		#GAME BOARD
		self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
		self.canvas.place(x=0, y=33)
		bgImg = Image.open('imgs/download.jpg')
		bgImg = bgImg.resize((self.width, self.height))
		bgImg = ImageTk.PhotoImage(bgImg)
		self.canvas.create_image( 0, 0, image = bgImg, anchor = "nw")
                     
		#create the middle horizontal line
		lineColor, lineWidth = 'brown4', 5
		self.canvas.create_line(0, self.height/2, self.width, self.height/2, width=lineWidth, fill=lineColor)
		#create the middle vertical line
		self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=lineWidth, fill=lineColor)
		#draw left diagonal ine
		self.canvas.create_line(0, 0, self.width, self.height, width=lineWidth, fill=lineColor)
		#draw right diagonal line
		self.canvas.create_line(self.width, 0, 0, self.height, width=lineWidth, fill=lineColor)

		self.position_0 = tk.Button(self.window, text=0, width=1, height=1, fg='grey', 
									bg='grey',activebackground='grey', activeforeground='grey',
									cursor='hand2', command=self.goToPosition_0)
		self.position_0.place(x=0,y=32)
		self.position_1 = tk.Button(self.window, text=1, width=1, height=1, fg='grey', 
									bg='grey',activebackground='grey', activeforeground='grey',
									cursor='hand2', command=self.goToPosition_1)
		self.position_1.place(x=self.width/2-8,y=32)
		self.position_2 = tk.Button(self.window, text=2, width=1, height=1, fg='grey', 
									bg='grey',activebackground='grey', activeforeground='grey',
									cursor='hand2', command=self.goToPosition_2)
		self.position_2.place(x=self.width-13,y=32)
		self.position_3 = tk.Button(self.window, text=3, width=1, height=1, fg='grey', 
									bg='grey',activebackground='grey', activeforeground='grey',
									cursor='hand2', command=self.goToPosition_3)
		self.position_3.place(x=0,y=self.height/2+20)
		self.position_4 = tk.Button(self.window, text=4, width=1, height=1, fg='grey', 
									bg='grey',activebackground='grey', activeforeground='grey',
									cursor='hand2', command=self.goToPosition_4)
		self.position_4.place(x=self.width/2-8,y=self.height/2+20)
		self.position_5 = tk.Button(self.window, text=5, width=1, height=1, fg='grey', 
									bg='grey',activebackground='grey', activeforeground='grey',
									cursor='hand2', command=self.goToPosition_5)
		self.position_5.place(x=self.width-13,y=self.height/2+20)
		self.position_6 = tk.Button(self.window, text=6, width=1, height=1, fg='grey', 
									bg='grey',activebackground='grey', activeforeground='grey',
									cursor='hand2', command=self.goToPosition_6)
		self.position_6.place(x=0,y=self.height+11)
		self.position_7 = tk.Button(self.window, text=7, width=1, height=1, fg='grey', 
									bg='grey',activebackground='grey', activeforeground='grey',
									cursor='hand2', command=self.goToPosition_7)
		self.position_7.place(x=self.width/2-10,y=self.height+11)
		self.position_8 = tk.Button(self.window, text=8, width=1, height=1, fg='grey', 
									bg='grey',activebackground='grey', activeforeground='grey',
									cursor='hand2', command=self.goToPosition_8)
		self.position_8.place(x=self.width-13,y=self.height+11)
		#GAME BOARD

		#create player 1 marbles
		self.player1Marble1 = tk.Button(self.window, text=9, width=2, height=1, bg=self.player1Color,
										fg=self.player1Color, activebackground=self.player1Color, 
										activeforeground=self.player1Color, command=self.p1m1)
		self.player1Marble1.place(x=self.width-65,y=self.height+40)
		self.player1Marble2 = tk.Button(self.window, text=9, width=2, height=1, bg=self.player1Color,
										fg=self.player1Color,activebackground=self.player1Color, 
										activeforeground=self.player1Color,command=self.p1m2)
		self.player1Marble2.place(x=self.width-100,y=self.height+40)
		self.player1Marble3 = tk.Button(self.window, text=9, width=2, height=1, bg=self.player1Color,
										fg=self.player1Color,activebackground=self.player1Color, 
										activeforeground=self.player1Color,command=self.p1m3)
		self.player1Marble3.place(x=self.width-135,y=self.height+40)

		#create player 2 marbles
		self.player2Marble1 = tk.Button(self.window, text=9, width=2, height=1, bg=self.player2Color,
										fg=self.player2Color,activebackground=self.player2Color, 
										activeforeground=self.player2Color,command=self.p2m1)
		self.player2Marble1.place(x=45,y=5)
		self.player2Marble2 = tk.Button(self.window, text=9, width=2, height=1, bg=self.player2Color,
										fg=self.player2Color, activebackground=self.player2Color, 
										activeforeground=self.player2Color,command=self.p2m2)
		self.player2Marble2.place(x=80,y=5)
		self.player2Marble3 = tk.Button(self.window, text=9, width=2, height=1, bg=self.player2Color,
										fg=self.player2Color, activebackground=self.player2Color, 
										activeforeground=self.player2Color,command=self.p2m3)
		self.player2Marble3.place(x=115,y=5)

		#creating the restart/forfeit buttons
		restartImg = tkinter.PhotoImage(file='imgs/restart.png')
		self.p1Restart = tkinter.Button(self.window, image=restartImg, bd=0, command=self.restartP1)
		self.p1Restart.place(x=80, y=self.height+38)
		self.p2Restart = tkinter.Button(self.window, image=restartImg, bd=0, command=self.restartP2)
		self.p2Restart.place(x=self.width-100, y=0)

		#creating scores label
		self.player1Score = tkinter.Label(self.window, text=0, font=('times new roman',17,'bold'))
		self.player1Score.place(x=self.width/2-10, y=self.height+40)
		self.player2Score = tkinter.Label(self.window, text=0, font=('times new roman',17,'bold'))
		self.player2Score.place(x=self.width/2-10, y=0)

		self.window.mainloop()

	def restart(self, player):
		ask = tkinter.messagebox.askyesno('Ask', 'You restart, your opponent wins. Are you sure you want to restart')
		if ask:
			if player == 1:
				self.player1Win = False
				self.player2Win = True
			else:
				self.player1Win = True
				self.player2Win = False
			self.player1Move = not self.player1Move
			self.checkWinner()

	def gameLogic(self, position):
		if self.clickedMarblePosition in self.possibleMoves[position]:
			if position == 1 or position == 4 or position == 7:
				x = self.positions[position][0]-4
				y = self.positions[position][1]
			elif position == 2 or position == 5 or position == 8:
				x = self.positions[position][0]-5
				y = self.positions[position][1]
			else:
				x = self.positions[position][0]
				y = self.positions[position][1]

			if self.clicked:
				self.clickedMarble.config(self.clickedMarble.place(x=x,y=y))
				self.clickedMarble.config(bd=2, text=position)
			self.clicked = False
			try:
				if self.clickedMarble.cget('text') == position:
					self.player1Move = not self.player1Move
			except AttributeError:
				pass

		self.checkWinner()

	def marbleMovement(self, player, marbleNumber):
		if player == 1:
			if self.player1Move:
				if marbleNumber == 1:
					self.clickedMarblePosition = self.player1Marble1.cget('text')
				elif marbleNumber == 2:
					self.clickedMarblePosition = self.player1Marble2.cget('text')
				else:
					self.clickedMarblePosition = self.player1Marble3.cget('text')
				if self.clicked:
					self.clickedMarble.config(bd=2)
				if marbleNumber == 1:
					self.clickedMarble = self.player1Marble1
					self.player1Marble1.config(bd=0)
				elif marbleNumber == 2:
					self.clickedMarble = self.player1Marble2
					self.player1Marble2.config(bd=0)
				else:
					self.clickedMarble = self.player1Marble3
					self.player1Marble3.config(bd=0)
				self.clicked = True

		if player == 2:
			if not self.player1Move:
				if marbleNumber == 1:
					self.clickedMarblePosition = self.player2Marble1.cget('text')
				elif marbleNumber == 2:
					self.clickedMarblePosition = self.player2Marble2.cget('text')
				else:
					self.clickedMarblePosition = self.player2Marble3.cget('text')
				if self.clicked:
					self.clickedMarble.config(bd=2)
				if marbleNumber == 1:
					self.clickedMarble = self.player2Marble1
					self.player2Marble1.config(bd=0)
				elif marbleNumber == 2:
					self.clickedMarble = self.player2Marble2
					self.player2Marble2.config(bd=0)
				else:
					self.clickedMarble = self.player2Marble3
					self.player2Marble3.config(bd=0)
				self.clicked = True

	def checkWinner(self):
		#check if player 1 wins
		if not self.player1Move:
			p1MarblePositions = [int(self.player1Marble1.cget('text')),
								 int(self.player1Marble2.cget('text')),
								 int(self.player1Marble3.cget('text'))
			]
			p1MarblePositions.sort()
			if (p1MarblePositions in self.rowWins or p1MarblePositions in self.columnWins or
				p1MarblePositions == self.leftDiagonalWins or p1MarblePositions == self.rightDiagonalWins):
				self.player1Win = True

		#check if player 2 wins
		else:
			p2MarblePositions = [int(self.player2Marble1.cget('text')),
								 int(self.player2Marble2.cget('text')),
								 int(self.player2Marble3.cget('text'))
			]
			p2MarblePositions.sort()
			if (p2MarblePositions in self.rowWins or p2MarblePositions in self.columnWins or
				p2MarblePositions == self.leftDiagonalWins or p2MarblePositions == self.rightDiagonalWins):
				self.player2Win = True

		if self.player1Win:
			winner = 'Player1'
			score = self.player1Score.cget('text') + 1
			self.player1Score.config(text=score)
		if self.player2Win:
			winner = 'Player2'
			score = self.player2Score.cget('text') + 1
			self.player2Score.config(text=score)

		if self.player1Win or self.player2Win:
			self.player1Win = False
			self.player2Win = False
			tkinter.messagebox.showinfo('Win', winner+' wins')

			#resetting marble positions
			self.player1Marble1.config(self.player1Marble1.place(x=self.width-65,y=self.height+40), text=9, bd=2)
			self.player1Marble2.config(self.player1Marble2.place(x=self.width-100,y=self.height+40), text=9, bd=2)
			self.player1Marble3.config(self.player1Marble3.place(x=self.width-135,y=self.height+40), text=9, bd=2)

			self.player2Marble1.config(self.player2Marble1.place(x=45,y=5), text=9, bd=2)
			self.player2Marble2.config(self.player2Marble2.place(x=80,y=5), text=9, bd=2)
			self.player2Marble3.config(self.player2Marble3.place(x=115,y=5), text=9, bd=2)

	def goToPosition_0(self):
		self.gameLogic(0)

	def goToPosition_1(self):
		self.gameLogic(1)

	def goToPosition_2(self):
		self.gameLogic(2)

	def goToPosition_3(self):
		self.gameLogic(3)

	def goToPosition_4(self):
		self.gameLogic(4)

	def goToPosition_5(self):
		self.gameLogic(5)

	def goToPosition_6(self):
		self.gameLogic(6)

	def goToPosition_7(self):
		self.gameLogic(7)

	def goToPosition_8(self):
		self.gameLogic(8)

	def p1m1(self):
		self.marbleMovement(1, 1)

	def p1m2(self):
		self.marbleMovement(1, 2)

	def p1m3(self):
		self.marbleMovement(1, 3)

	def p2m1(self):
		self.marbleMovement(2, 1)

	def p2m2(self):
		self.marbleMovement(2, 2)

	def p2m3(self):
		self.marbleMovement(2, 3)

	def restartP1(self):
		self.restart(1)
	
	def restartP2(self):
		self.restart(2)

game = Game()