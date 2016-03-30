import sys
import random
import signal
import copy

class Player63:
	
	def __init__(self):
		pass



	def detBlkOpen(self,old_move, block_stat):
		blk_all = []
		if old_move[0]  == -1 and old_move[1] == -1:
			blk_all = [7]

		elif old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
			blk_all = [1,3]
	
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 0:
			blk_all = [3,7]

		elif old_move[0] % 3 == 0 and old_move[1] % 3 == 2:
			blk_all = [1,5]

		elif old_move[0] % 3 == 0 and old_move[1] % 3 == 1:
			blk_all = [0,2]
	
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 2:
			blk_all = [5,7]

		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 1:
			blk_all = [6,8]

		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 0:
			blk_all = [0,6]

		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 2:
			blk_all = [2,8]

		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 1:
			blk_all = [4]
		else:
			sys.exit(1)
		final_blk_all = []
		for i in blk_all:
			if block_stat[i] == '-':
				final_blk_all.append(i)
		return final_blk_all
	

	def getEmptyCells(self,gameboard,block_stat,blk_all):
		cells = []
		for idb in blk_all:
			id1 = idb/3
			id2 = idb%3
			for i in range(id1*3,id1*3+3):
				for j in range(id2*3,id2*3+3):
					if gameboard[i][j] == '-':
						cells.append((i,j))
	
		if cells == []:
			blk_all = []
			for i in range(0,9):
				if block_stat[i] == '-':
					blk_all.append(i)
			for idb in blk_all:
				id1 = idb/3
				id2 = idb%3
				for i in range(id1*3,id1*3+3):
					for j in range(id2*3,id2*3+3):
						if gameboard[i][j] == '-':
							cells.append((i,j))

		return (cells,len(cells))

		
	def checkRowUtil(self,gameboard,flag,cell):
		row = cell[0]
		col = cell[1]
		if col%3 == 0:
			if gameboard[row][col+1] == gameboard[row][col+2]:
				if gameboard[row][col+1] == '-':
					return 4
				elif gameboard[row][col+1] == flag:
					return 100
				else:
					return 25
			else:
				if gameboard[row][col+1] == '-' and gameboard[row][col+2] == flag or gameboard[row][col+1] == flag and gameboard[row][col+2] == '-': 			
					return 10
	
				elif gameboard[row][col+1] == flag or gameboard[row][col+2] == flag:
					return 0
				else:
					return 2

		elif col%3 == 1:
			if gameboard[row][col+1] == gameboard[row][col-1]:
				if gameboard[row][col+1] == '-':
					return 4
				elif gameboard[row][col+1] == flag:
					return 100
				else:
					return 25
			else:
				if gameboard[row][col+1] == '-' and gameboard[row][col-1] == flag or gameboard[row][col+1] == flag and gameboard[row][col-1] == '-': 			
					return 10
	
				elif gameboard[row][col+1] == flag or gameboard[row][col-1] == flag:
					return 0
				else:
					return 2
		else:
			if gameboard[row][col-1] == gameboard[row][col-2]:
				if gameboard[row][col-1] == '-':
					return 4
				elif gameboard[row][col-1] == flag:
					return 100
				else:
					return 25
			else:
				if gameboard[row][col-1] == '-' and gameboard[row][col-2] == flag or gameboard[row][col-1] == flag and gameboard[row][col-2] == '-': 			
					return 10
	
				elif gameboard[row][col-1] == flag or gameboard[row][col-2] == flag:
					return 0
				else:
					return 2
			


	def checkColUtil(self,gameboard,flag,cell):
		row = cell[0]
		col = cell[1]
		if row%3 == 0:
			if gameboard[row+1][col] == gameboard[row+2][col]:
				if gameboard[row+1][col] == '-':
					return 4
				elif gameboard[row+1][col] == flag:
					return 100
				else:
					return 25
			else:
				if gameboard[row+1][col] == '-' and gameboard[row+2][col] == flag or gameboard[row+1][col] == flag and gameboard[row+2][col] == '-': 			
					return 10
	
				elif gameboard[row+1][col] == flag or gameboard[row+2][col] == flag:
					return 0
				else:
					return 2

		elif row%3 == 1:
			if gameboard[row+1][col] == gameboard[row-1][col]:
				if gameboard[row+1][col] == '-':
					return 4
				elif gameboard[row+1][col] == flag:
					return 100
				else:
					return 25
			else:
				if gameboard[row+1][col] == '-' and gameboard[row-1][col] == flag or gameboard[row+1][col] == flag and gameboard[row-1][col] == '-': 			
					return 10
	
				elif gameboard[row+1][col] == flag or gameboard[row-1][col] == flag:
					return 0
				else:
					return 2
		else:
			if gameboard[row-1][col] == gameboard[row-2][col]:
				if gameboard[row-1][col] == '-':
					return 4
				elif gameboard[row-1][col] == flag:
					return 100
				else:
					return 25
			else:
				if gameboard[row-1][col] == '-' and gameboard[row-2][col] == flag or gameboard[row-1][col] == flag and gameboard[row-2][col] == '-': 			
					return 10
	
				elif gameboard[row-1][col] == flag or gameboard[row-2][col] == flag:
					return 0
				else:
					return 2


		
	def checkDiagUtil(self,gameboard,flag,cell):
		row = cell[0]
		col = cell[1]
		d1 = 0
		d2 = 0
		if ((row%3)+(col%3))%2 == 1:
			return 0
		else:
			
			if row%3 == 1 and col%3 == 1:
				if gameboard[row-1][col-1] == gameboard[row+1][col+1]:
					if gameboard[row+1][col+1] == '-':
						d1 = 4
					elif gameboard[row+1][col+1] == flag:
						d1 = 100
					else:
						d1 = 25
				else:
					if gameboard[row+1][col+1] == '-' and gameboard[row-1][col-1] == flag or gameboard[row+1][col+1] == flag and gameboard[row-1][col-1] == '-': 			
						d1 = 10
		
					elif gameboard[row+1][col+1] == flag or gameboard[row-1][col-1] == flag:
						d1 = 0
					else:
						d1 = 2


				if gameboard[row-1][col+1] == gameboard[row+1][col-1]:
					if gameboard[row+1][col-1] == '-':
						d2 = 4
					elif gameboard[row+1][col-1] == flag:
						d2 = 100
					else:
						d2 = 25
				else:
					if gameboard[row+1][col-1] == '-' and gameboard[row-1][col+1] == flag or gameboard[row+1][col-1] == flag and gameboard[row-1][col+1] == '-': 			
						d2 = 10
		
					elif gameboard[row+1][col-1] == flag or gameboard[row-1][col+1] == flag:
						d2 = 0
					else:
						d2 = 2
				
				return d1 + d2

			elif row%3 == col%3:
				if row%3 == 0:
					if gameboard[row+1][col+1] == gameboard[row+2][col+2]:
						if gameboard[row+1][col+1] == '-':
							return 4
						elif gameboard[row+1][col+1] == flag:
							return 100
						else:
							return 25
					else:
						if gameboard[row+1][col+1] == '-' and gameboard[row+2][col+2] == flag or gameboard[row+1][col+1] == flag and gameboard[row+2][col+2] == '-': 			
							return 10
		
						elif gameboard[row+1][col+1] == flag or gameboard[row+2][col+2] == flag:
							return 0
						else:
							return 2
				else:
					if gameboard[row-1][col-1] == gameboard[row-2][col-2]:
						if gameboard[row-1][col-1] == '-':
							return 4
						elif gameboard[row-1][col-1] == flag:
							return 100
						else:
							return 25
					else:
						if gameboard[row-1][col-1] == '-' and gameboard[row-2][col-2] == flag or gameboard[row-1][col-1] == flag and gameboard[row-2][col-2] == '-': 			
							return 10
		
						elif gameboard[row-1][col-1] == flag or gameboard[row-2][col-2] == flag:
							return 0
						else:
							return 2

			else:
				if row%3 == 0:
					if gameboard[row+1][col-1] == gameboard[row+2][col-2]:
						if gameboard[row+1][col-1] == '-':
							return 4
						elif gameboard[row+1][col-1] == flag:
							return 100
						else:
							return 25
					else:
						if gameboard[row+1][col-1] == '-' and gameboard[row+2][col-2] == flag or gameboard[row+1][col-1] == flag and gameboard[row+2][col-2] == '-': 			
							return 10
		
						elif gameboard[row+1][col-1] == flag or gameboard[row+2][col-2] == flag:
							return 0
						else:
							return 2
					
				else:
					if gameboard[row-1][col+1] == gameboard[row-2][col+2]:
						if gameboard[row-1][col+1] == '-':
							return 4
						elif gameboard[row-1][col+1] == flag:
							return 100
						else:
							return 25
					else:
						if gameboard[row-1][col+1] == '-' and gameboard[row-2][col+2] == flag or gameboard[row-1][col+1] == flag and gameboard[row-2][col+2] == '-': 			
							return 10
		
						elif gameboard[row-1][col+1] == flag or gameboard[row-2][col+2] == flag:
							return 0
						else:
							return 2

	
		

	def findMaxUtil(self,block_util,dict_util,block_stat):
		maxVal = -100000
		maxCell = (-1,-1)
		count = 0
		factor1 = 1
		factor2 = 1
		for i in range(0,9):
			if block_stat[i] == '-':
				count+=1

		count = 9 - count
		factor1 = count/3 + 0.5

		for c in dict_util:
			row_c = c[0]*9
			col_c = c[1]	
			block_num = (row_c + col_c)/9
			if maxVal <= block_util[block_num]*factor1 + dict_util[c]*factor2:
				maxVal = block_util[block_num]*factor1 + dict_util[c]*factor2
				maxCell = c	
		
		return (maxCell,maxVal)

	def findBestMax(self,dict_util):
		maxVal = -100000
		maxCell = (-1,-1)
		for c in dict_util:
			if maxVal <= dict_util[c]:
				maxVal = dict_util[c]
				maxCell = c	

		#print "(BEST)Max Player: ",maxCell,maxVal
		return (maxCell,maxVal)

	def findBestMin(self,dict_util):
		minVal = 100000
		minCell = (-1,-1)
		for c in dict_util:
			if minVal >= dict_util[c]:
				minVal = dict_util[c]
				minCell = c	


		#print "(BEST)Min Player: ",minCell,minVal
		return (minCell,minVal)

	def bestChoice(self,gameboard, blk_all,block_stat,block_util,flag,cells):
		i=0
		util=[]
		dict_util={}
		for c in cells:
			util.append(0)
			util[i]+=self.checkRowUtil(gameboard,flag,c)
			util[i]+=self.checkColUtil(gameboard,flag,c)	
			util[i]+=self.checkDiagUtil(gameboard,flag,c)	
			dict_util[c]=util[i] 
			#print "Base case moves:- ",c,util[i]
			i=i+1
			

		#bestCell,bestVal = self.findMaxUtil(block_util,dict_util,block_stat)
		best = self.findMaxUtil(block_util,dict_util,block_stat)
		bestCell = best[0]
		bestVal = best[1]
		#print "(MAXIMUM) Base case move:- ",bestCell,bestVal
		if bestCell == (-1,-1):
			bestVal = 0
		return (bestCell,bestVal)
		  
	def checkBlockUtil(self,gameboard,block_stat,flag):
		i=0
		util=[]
		for b in range(0,9):	
			row_b = b/3
			col_b = b%3
			util.append(0)
			util[i]+=self.checkRowUtil(block_stat,flag,(row_b,col_b))	
			util[i]+=self.checkColUtil(block_stat,flag,(row_b,col_b))	
			util[i]+=self.checkDiagUtil(block_stat,flag,(row_b,col_b))	
			i=i+1
		return util

	def convertBlock(self,block_stat):
		new_block_stat=[]
		new_block_stat.append([])
		for i in range(0,3):
			new_block_stat[0].append(block_stat[i])

		new_block_stat.append([])
		for i in range(3,6):
			new_block_stat[1].append(block_stat[i])

		new_block_stat.append([])
		for i in range(6,9):
			new_block_stat[2].append(block_stat[i])

		return new_block_stat

	def isWon(self,gameboard,bs,block_num,flag,action):
		gb = gameboard
		ir = (block_num/3)*3    #ir - init_row
		ic = (block_num%3)*3    #ic - init_col
		row = action[0]
		col = action[1]
		#print "row: ",row,"col: ",col
		#print "tuple",ir,ic
		#print "BlockNum: ",block_num

		if (gb[ir][ic] == gb[ir][ic+1] and gb[ir][ic+1] == gb[ir][ic+2] and gb[ir][ic] == flag and row == ir and (col/3)*3 == ic) or (gb[ir+1][ic] == gb[ir+1][ic+1] and gb[ir+1][ic+1] == gb[ir+1][ic+2] and gb[ir+1][ic] == flag and row == ir+1 and (col/3)*3 == ic) or (gb[ir+2][ic] == gb[ir+2][ic+1] and gb[ir+2][ic+1] == gb[ir+2][ic+2] and gb[ir+2][ic] == flag and row == ir+2 and (col/3)*3 == ic):
			return True	

		elif (gb[ir][ic] == gb[ir+1][ic] and gb[ir+1][ic] == gb[ir+2][ic] and gb[ir][ic] == flag and col == ic and (row/3)*3 == ir) or (gb[ir][ic+1] == gb[ir+1][ic+1] and gb[ir+1][ic+1] == gb[ir+2][ic+1] and gb[ir][ic+1] == flag and col == ic+1 and (row/3)*3 == ir) or (gb[ir][ic+2] == gb[ir+1][ic+2] and gb[ir+1][ic+2] == gb[ir+2][ic+2] and gb[ir][ic+2] == flag and col == ic+2 and (row/3)*3 == ir):
			return True	

		elif (gb[ir][ic] == gb[ir+1][ic+1] and gb[ir][ic] == gb[ir+2][ic+2] and gb[ir+1][ic+1] == flag and (row%3) == (col%3)) or (gb[ir][ic+2] == gb[ir+1][ic+1] and gb[ir+1][ic+1] == gb[ir+2][ic] and gb[ir+1][ic+1] == flag and (row%3) == (2-(col%3))):
			return True
		
		else:
			return False


	def checkWin(self,game_board,block_stat,flag):
		bs = block_stat
		if (bs[0] == bs[1] and bs[1] == bs[2] and bs[1] == flag) or (bs[3] == flag and bs[3] == bs[4] and bs[4] == bs[5]) or (bs[6] == flag and bs[6] == bs[7] and bs[7] == bs[8]):
			return True
		elif (bs[0] == bs[3] and bs[3] == bs[6] and bs[0] == flag) or (bs[1] == bs[4] and bs[4] == bs[7] and bs[4] == flag) or (bs[2] == bs[5] and bs[5] == bs[8] and bs[5] == flag):
			return True
		elif (bs[0] == bs[4] and bs[4] == bs[8] and bs[0] == flag) or (bs[2] == bs[4] and bs[4] == bs[6] and bs[2] == flag):
			return True
		else:
		 	return False

	def convertToBlock(self,row,col):	
		block = (row/3)*3 + (col/3)	
		return block 

	def update_board(self,gameboard,block_stat,flag,a):
		row = a[0]
		col = a[1]
		block_num = self.convertToBlock(row,col)
		blk_win = False
		gameboard[row][col] = flag
		#print "In update_board: ",row,col,block_num
		if(self.isWon(gameboard,block_stat,block_num,flag,a)):
			block_stat[block_num] = flag
			blk_win = True

		return (gameboard,block_stat,blk_win)

	def printboard(self,gb,bs):
		print '=========== OUR Board ==========='
		for i in range(9):
			if i > 0 and i % 3 == 0:
				print
			for j in range(9):
				if j > 0 and j % 3 == 0:
					print " " + gb[i][j],
				else:
					print gb[i][j],

			print
		print "=================================="

		print "=========== OUR Block Status ========="
		for i in range(0, 9, 3):
			print bs[i] + " " + bs[i+1] + " " + bs[i+2] 
		print "=================================="
		print


	def getAllEmpty(self,gb):
		count = 0
		for i in range(9):
			for j in range(9):
				if gb[i][j] == '-':
					count+=1

		return count

	def minimax(self,gameboard,block_stat,old_move,flag,player,depth,alpha,beta,base):
		if depth >= base:
			temp_board = gameboard
			temp_block = block_stat
			blk_all  = self.detBlkOpen(old_move, temp_block)
			#cells,length = self.getEmptyCells(temp_board,temp_block,blk_all)
			cl = self.getEmptyCells(gameboard,block_stat,blk_all)
			cells = cl[0]
			length = cl[1]
			temp_new_block = self.convertBlock(temp_block)
			block_util = self.checkBlockUtil(temp_board,temp_new_block,flag)
			t = self.bestChoice(temp_board,blk_all,temp_block,block_util,flag,cells)
			cell = t[0]
			utility = t[1]
			alpha = utility
			beta = utility
			return t

		if player == 1:
			dict_util={}
			blk_all  = self.detBlkOpen(old_move, block_stat)
			#cells,length = self.getEmptyCells(gameboard,block_stat,blk_all)					
			cl = self.getEmptyCells(gameboard,block_stat,blk_all)
			cells = cl[0]
			length = cl[1]
			if cells == []:
				return ((-1,-1),10000)
			for a in cells:
				if depth == 0:
					alpha = -10000
					beta = 10000
				temp_board = copy.deepcopy(gameboard)
				temp_block = copy.deepcopy(block_stat)
				#temp_board = gameboard[:]
				#temp_block = block_stat[:]
				alpha1 = copy.deepcopy(alpha)
				beta1 = copy.deepcopy(beta)
				#temp_board1,temp_block1,blockWin = self.update_board(temp_board,temp_block,flag,a)
				temp = self.update_board(temp_board,temp_block,flag,a)
				temp_board1 = temp[0]
				temp_block1 = temp[1]
				blockWin = temp[2]
				won = self.checkWin(temp_board1,temp_block1,flag);
				if flag == 'x':
					t = self.minimax(temp_board1,temp_block1,a,'o',0,depth+1,alpha1,beta1,base)
					value = t[1]
					if blockWin:
						dict_util[a] = value + 20
					else:
						dict_util[a] = value
					if won:
						dict_util[a] = (2100 - (depth*20))
				elif flag == 'o':
					t = self.minimax(temp_board1,temp_block1,a,'x',0,depth+1,alpha1,beta1,base)
					value = t[1]
					if blockWin:
						dict_util[a] = value + 20
					else:
						dict_util[a] = value
					if won:
						dict_util[a] = (2100 - (depth*20))

				if alpha <= dict_util[a]:
					alpha = dict_util[a]
					utility = alpha
				if alpha >= beta:
					break
			#move,alpha = self.findBestMax(dict_util)
			#if depth == 0:
			#	print "MAX utils: ",dict_util
			fbm = self.findBestMax(dict_util)
			move = fbm[0]
			alpha = fbm[1]
			utility = alpha
			return (move,alpha)

		if player == 0:
			dict_util={}
			blk_all  = self.detBlkOpen(old_move, block_stat)
			#cells,length = self.getEmptyCells(gameboard,block_stat,blk_all)
			cl = self.getEmptyCells(gameboard,block_stat,blk_all)
			cells = cl[0]
			length = cl[1]
			if cells == []:
				return ((-1,-1),-10000)
			for a in cells:
				temp_board = copy.deepcopy(gameboard)
				temp_block = copy.deepcopy(block_stat)
				#temp_board = gameboard[:]
				#temp_block = block_stat[:]
				alpha1 = copy.deepcopy(alpha)
				beta1 = copy.deepcopy(beta)
				#temp_board1,temp_block1,blockWin = self.update_board(temp_board,temp_block,flag,a)
				temp = self.update_board(temp_board,temp_block,flag,a)
				temp_board1 = temp[0]
				temp_block1 = temp[1]
				blockWin = temp[2]
				won = self.checkWin(temp_board1,temp_block1,flag)
				if flag == 'x':
					t = self.minimax(temp_board1,temp_block1,a,'o',1,depth+1,alpha1,beta1,base)
					value = t[1]
					if blockWin:
						dict_util[a] = value - 40
					else:
						dict_util[a] = value
					if won:
						dict_util[a] = -2100 + (depth*20)
				elif flag == 'o':
					t = self.minimax(temp_board1,temp_block1,a,'x',1,depth+1,alpha1,beta1,base)
					value = t[1]
					if blockWin:
						dict_util[a] = value - 40
					else:
						dict_util[a] = value
					if won:
						dict_util[a] = -2100 + (depth*20)
						
				if beta >= dict_util[a]:
					beta = dict_util[a]
					utility = beta

				if alpha >= beta:
					break

			#move,beta = self.findBestMin(dict_util)
			#if depth == 1:
			#	print "MIN utils: ",dict_util
			fbm = self.findBestMin(dict_util)
			move = fbm[0]
			beta = fbm[1]
			utility = beta
			return (move,beta)
			
	def move(self,temp_board,temp_block,old_move,flag):
		#print "alphaBeta(Shruti) with depth 5"
		temp_temp_board = copy.deepcopy(temp_board)
		temp_temp_block = copy.deepcopy(temp_block)
		#temp_temp_board = temp_board[:]
		#temp_temp_block = temp_block[:]
		base = 5
		blk_all  = self.detBlkOpen(old_move, temp_block)
		m = self.getEmptyCells(temp_board,temp_block,blk_all)
		cells = m[0]
		length = m[1]
		cls = self.getAllEmpty(temp_board)
		if length < 5 and cls < 45:
			base = 7
		elif length < 10 and cls < 45:
			base = 6
		elif length < 38:
			base = 5
		else:
			base = 4
		t = self.minimax(temp_board,temp_block,old_move,flag,1,0,-10000,10000,base)
		cell = t[0]
		utility = t[1]
		#return cells[random.randrange(len(cells))]
		print "Our Bot's move: ",cell
		return cell



''' Our bot is P1 (x)
=========== Game Board ===========
- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -
==================================
=========== Block Status =========
- - -
- - -
- - -
==================================

Player 1 made the move: (8, 4) with x
=========== Game Board ===========
- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - -
- - -
- - -
==================================

Player 2 made the move: (6, 1) with o
=========== Game Board ===========
- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- o -  - - -  - - -
- - -  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - -
- - -
- - -
==================================

Player 1 made the move: (1, 6) with x
=========== Game Board ===========
- - -  - - -  - - -
- - -  - - -  x - -
- - -  - - -  - - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- o -  - - -  - - -
- - -  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - -
- - -
- - -
==================================

Player 2 made the move: (7, 2) with o
=========== Game Board ===========
- - -  - - -  - - -
- - -  - - -  x - -
- - -  - - -  - - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- o -  - - -  - - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - -
- - -
- - -
==================================

Player 1 made the move: (0, 6) with x
=========== Game Board ===========
- - -  - - -  x - -
- - -  - - -  x - -
- - -  - - -  - - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- o -  - - -  - - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - -
- - -
- - -
==================================

Player 2 made the move: (1, 5) with o
=========== Game Board ===========
- - -  - - -  x - -
- - -  - - o  x - -
- - -  - - -  - - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- o -  - - -  - - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - -
- - -
- - -
==================================

Player 1 made the move: (2, 6) with x
=========== Game Board ===========
- - -  - - -  x - -
- - -  - - o  x - -
- - -  - - -  x - -

- - -  - - -  - - -
- - -  - - -  - - -
- - -  - - -  - - -

- o -  - - -  - - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (5, 1) with o
=========== Game Board ===========
- - -  - - -  x - -
- - -  - - o  x - -
- - -  - - -  x - -

- - -  - - -  - - -
- - -  - - -  - - -
- o -  - - -  - - -

- o -  - - -  - - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (6, 6) with x
=========== Game Board ===========
- - -  - - -  x - -
- - -  - - o  x - -
- - -  - - -  x - -

- - -  - - -  - - -
- - -  - - -  - - -
- o -  - - -  - - -

- o -  - - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (4, 1) with o
=========== Game Board ===========
- - -  - - -  x - -
- - -  - - o  x - -
- - -  - - -  x - -

- - -  - - -  - - -
- o -  - - -  - - -
- o -  - - -  - - -

- o -  - - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (3, 5) with x
=========== Game Board ===========
- - -  - - -  x - -
- - -  - - o  x - -
- - -  - - -  x - -

- - -  - - x  - - -
- o -  - - -  - - -
- o -  - - -  - - -

- o -  - - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (2, 3) with o
=========== Game Board ===========
- - -  - - -  x - -
- - -  - - o  x - -
- - -  o - -  x - -

- - -  - - x  - - -
- o -  - - -  - - -
- o -  - - -  - - -

- o -  - - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (4, 0) with x
=========== Game Board ===========
- - -  - - -  x - -
- - -  - - o  x - -
- - -  o - -  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o -  - - -  - - -

- o -  - - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (0, 1) with o
=========== Game Board ===========
- o -  - - -  x - -
- - -  - - o  x - -
- - -  o - -  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o -  - - -  - - -

- o -  - - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (0, 2) with x
=========== Game Board ===========
- o x  - - -  x - -
- - -  - - o  x - -
- - -  o - -  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o -  - - -  - - -

- o -  - - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (0, 3) with o
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - -  o - -  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o -  - - -  - - -

- o -  - - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (5, 2) with x
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - -  o - -  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o x  - - -  - - -

- o -  - - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (6, 3) with o
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - -  o - -  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o x  - - -  - - -

- o -  o - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (2, 5) with x
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - -  o - x  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o x  - - -  - - -

- o -  o - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (5, 6) with o
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - -  o - x  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o x  - - -  o - -

- o -  o - -  x - -
- - o  - - -  - - -
- - -  - x -  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (8, 5) with x
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - -  o - x  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o x  - - -  o - -

- o -  o - -  x - -
- - o  - - -  - - -
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (5, 8) with o
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - -  o - x  x - -

- - -  - - x  - - -
x o -  - - -  - - -
- o x  - - -  o - o

- o -  o - -  x - -
- - o  - - -  - - -
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (3, 7) with x
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - -  o - x  x - -

- - -  - - x  - x -
x o -  - - -  - - -
- o x  - - -  o - o

- o -  o - -  x - -
- - o  - - -  - - -
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (2, 2) with o
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - -  - - -
- o x  - - -  o - o

- o -  o - -  x - -
- - o  - - -  - - -
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (4, 7) with x
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - -  - x -
- o x  - - -  o - o

- o -  o - -  x - -
- - o  - - -  - - -
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (4, 5) with o
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - - -  o - o

- o -  o - -  x - -
- - o  - - -  - - -
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (7, 8) with x
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - - -  o - o

- o -  o - -  x - -
- - o  - - -  - - x
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (7, 6) with o
=========== Game Board ===========
- o x  o - -  x - -
- - -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - - -  o - o

- o -  o - -  x - -
- - o  - - -  o - x
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (1, 1) with x
=========== Game Board ===========
- o x  o - -  x - -
- x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - - -  o - o

- o -  o - -  x - -
- - o  - - -  o - x
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (5, 4) with o
=========== Game Board ===========
- o x  o - -  x - -
- x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - o -  o - o

- o -  o - -  x - -
- - o  - - -  o - x
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (6, 7) with x
=========== Game Board ===========
- o x  o - -  x - -
- x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - o -  o - o

- o -  o - -  x x -
- - o  - - -  o - x
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (1, 0) with o
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - o -  o - o

- o -  o - -  x x -
- - o  - - -  o - x
- - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (8, 0) with x
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - o -  o - o

- o -  o - -  x x -
- - o  - - -  o - x
x - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 2 made the move: (6, 5) with o
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - o -  o - o

- o -  o - o  x x -
- - o  - - -  o - x
x - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - -
- - -
==================================

Player 1 made the move: (5, 7) with x
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - o -  o x o

- o -  o - o  x x -
- - o  - - -  o - x
x - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - x
- - -
==================================

Player 2 made the move: (7, 0) with o
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - o -  o x o

- o -  o - o  x x -
o - o  - - -  o - x
x - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - x
- - -
==================================

Player 1 made the move: (7, 1) with x
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  - o -  o x o

- o -  o - o  x x -
o x o  - - -  o - x
x - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - x
- - -
==================================

Player 2 made the move: (5, 3) with o
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- - o  o - x  x - -

- - -  - - x  - x -
x o -  - - o  - x -
- o x  o o -  o x o

- o -  o - o  x x -
o x o  - - -  o - x
x - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - x
- - -
==================================

Player 1 made the move: (3, 1) with x
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- - o  o - x  x - -

- x -  - - x  - x -
x o -  - - o  - x -
- o x  o o -  o x o

- o -  o - o  x x -
o x o  - - -  o - x
x - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - x
- - -
==================================

Player 2 made the move: (2, 1) with o
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- o o  o - x  x - -

- x -  - - x  - x -
x o -  - - o  - x -
- o x  o o -  o x o

- o -  o - o  x x -
o x o  - - -  o - x
x - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - x
- - -
==================================

Player 1 made the move: (6, 8) with x
=========== Game Board ===========
- o x  o - -  x - -
o x -  - - o  x - -
- o o  o - x  x - -

- x -  - - x  - x -
x o -  - - o  - x -
- o x  o o -  o x o

- o -  o - o  x x x
o x o  - - -  o - x
x - -  - x x  - - -
==================================
=========== Block Status =========
- - x
- - x
- - x
==================================

P1
COMPLETE
'''

