import numpy as np
import random
import copy

class MinesweeperState:

    def __init__(self, size, mines):
        self._gridsize = size #ex: grid_size is 8 then board is 8x8
        self._minecount = mines #number of mines on the board
        self._myboard = np.full((size*size), -3, dtype=int)
        self._realboard = np.zeros((size*size), dtype=int) #full board information
        self._first = True
        #self._zero = (0,0)
        return


#MINES = -1     FLAGS = -2    BLANK/UNCLICKED = -3
    def randomize(self, seed=None):
        self._first = True
        if seed is not None:
            np.random.seed(seed)
        minepositions = np.zeros((self._minecount), dtype=int)
        self._realboard = np.zeros((self._gridsize*self._gridsize), dtype=int)
        self._myboard = np.full((self._gridsize*self._gridsize), -3)
        minepositions = random.sample(range(self._gridsize*self._gridsize), self._minecount)
        for m in minepositions:
            self._realboard[m] = -1
        for slot in range(self._gridsize*self._gridsize):
            if self._realboard[slot] == -1: continue
            col = slot % self._gridsize
            row = slot // self._gridsize
            nearby_minecount = 0
            if slot > self._gridsize*self._gridsize-1: continue
            if row > 0: #we can check up
                if self._realboard[slot-self._gridsize] == -1:
                    nearby_minecount += 1
            if col > 0: #we can check left
                if self._realboard[slot-1] == -1:
                    nearby_minecount += 1
            if row < self._gridsize-1: #we can check down
                if self._realboard[slot+self._gridsize] == -1:
                    nearby_minecount += 1
            if col < self._gridsize-1: #we can check right
                if self._realboard[slot+1] == -1:
                    nearby_minecount += 1
            if row > 0 and col > 0: #we can check upleft
                if self._realboard[slot-self._gridsize-1] == -1:
                    nearby_minecount += 1
            if row > 0 and col < self._gridsize-1: #we can check upright
                if self._realboard[slot-self._gridsize+1] == -1:
                    nearby_minecount += 1
            if row < self._gridsize-1 and col > 0: #we can check downleft
                if self._realboard[slot+self._gridsize-1] == -1:
                    nearby_minecount += 1
            if row < self._gridsize-1 and col < self._gridsize-1: #we can check downright
                if self._realboard[slot+self._gridsize+1] == -1:
                    nearby_minecount += 1
            self._realboard[slot] = nearby_minecount
        return self._myboard

    def turn(self, action):
        row, col, choice = action
        slot = (row*self._gridsize)+col
        if self._first and self._realboard[slot] == -1:
            while self._realboard[slot] == -1:
                self.randomize()
        self._first = False #no longer our first move, we can get blown up now
        # 0 = click, 1 = flag, 2 = remove flag
        if choice == 0: #if not a mine show tile value on users board
            self._myboard[slot] = self._realboard[slot]
            if self._myboard[slot] == 0:
                self.all_zeros(slot)
        elif choice == 1: #place a flag on users board tile
            self._myboard[slot] = -2
        elif choice == 2:
            if self._myboard[slot] == -2: #remove flag from user tile
                self._myboard[slot] = -3 #make the tile blank again
        #return

    def zero_neighbors(self):
        for slot in range(self._gridsize*self._gridsize):
            if slot > self._gridsize*self._gridsize-1: continue
            if self._myboard[slot] == 0:
                col = slot % self._gridsize
                row = slot // self._gridsize
                if row > 0: #we can check up
                    self._myboard[slot-self._gridsize] = self._realboard[slot-self._gridsize]
                if col > 0: #we can check left
                    self._myboard[slot-1] = self._realboard[slot-1]
                if row < self._gridsize-1: #we can check down
                    self._myboard[slot+self._gridsize] = self._realboard[slot+self._gridsize]
                if col < self._gridsize-1: #we can check right
                    self._myboard[slot+1] = self._realboard[slot+1]
                if row > 0 and col > 0: #we can check upleft
                    self._myboard[slot-self._gridsize-1] = self._realboard[slot-self._gridsize-1]
                if row > 0 and col < self._gridsize-1: #we can check upright
                    self._myboard[slot-self._gridsize+1] = self._realboard[slot-self._gridsize+1]
                if row < self._gridsize-1 and col > 0: #we can check downleft
                    self._myboard[slot+self._gridsize-1] = self._realboard[slot+self._gridsize-1]
                if row < self._gridsize-1 and col < self._gridsize-1: #we can check downright
                    self._myboard[slot+self._gridsize+1] = self._realboard[slot+self._gridsize+1]
        #return self._myboard

    def all_zeros(self, slot):
        col = slot % self._gridsize
        row = slot // self._gridsize
        if row > 0: #we can check up
            if self._realboard[((row-1)*self._gridsize)+col] == 0:
                if self._myboard[((row-1)*self._gridsize)+col] != 0: #if we havent already revealed the tile
                    self._myboard[((row-1)*self._gridsize)+col] = self._realboard[((row-1)*self._gridsize)+col]
                    self.recursive_all_zeros(row-1, col)
        if col > 0: #we can check left
            if self._realboard[(row*self._gridsize)+col-1] == 0:
                if self._myboard[(row*self._gridsize)+col-1] != 0: #if we havent already revealed the tile
                    self._myboard[(row*self._gridsize)+col-1] = self._realboard[(row*self._gridsize)+col-1]
                    self.recursive_all_zeros(row, col-1)
        if row < self._gridsize-1: #we can check down
            if self._realboard[((row+1)*self._gridsize)+col] == 0:
                if self._myboard[((row+1)*self._gridsize)+col] != 0: #if we havent already revealed the tile
                    self._myboard[((row+1)*self._gridsize)+col] = self._realboard[((row+1)*self._gridsize)+col]
                    self.recursive_all_zeros(row+1, col)
        if col < self._gridsize-1: #we can check right
            if self._realboard[(row*self._gridsize)+col+1] == 0:
                if self._realboard[(row*self._gridsize)+col+1] != 0: #if we havent already revealed the tile
                    self._myboard[(row*self._gridsize)+col+1] = self._realboard[(row*self._gridsize)+col+1]
                    self.recursive_all_zeros(row, col+1)
        self.zero_neighbors()
        return self._myboard

    def recursive_all_zeros(self, row, col):
        if row > 0: #we can check up
            if self._realboard[((row-1)*self._gridsize)+col] == 0:
                if self._myboard[((row-1)*self._gridsize)+col] != 0: #if we havent already revealed the tile
                    self._myboard[((row-1)*self._gridsize)+col] = self._realboard[((row-1)*self._gridsize)+col]
                    self.recursive_all_zeros(row-1, col)

        if col > 0: #we can check left
            if self._realboard[(row*self._gridsize)+col-1] == 0:
                if self._myboard[(row*self._gridsize)+col-1] != 0: #if we havent already revealed the tile
                    self._myboard[(row*self._gridsize)+col-1] = self._realboard[(row*self._gridsize)+col-1]
                    self.recursive_all_zeros(row, col-1)

        if row < self._gridsize-1: #we can check down
            if self._realboard[((row+1)*self._gridsize)+col] == 0:
                if self._myboard[((row+1)*self._gridsize)+col] != 0: #if we havent already revealed the tile
                    self._myboard[((row+1)*self._gridsize)+col] = self._realboard[((row+1)*self._gridsize)+col]
                    self.recursive_all_zeros(row+1, col)

        if col < self._gridsize-1: #we can check right
            if self._realboard[(row*self._gridsize)+col+1] == 0:
                if self._realboard[(row*self._gridsize)+col+1] != 0: #if we havent already revealed the tile
                    self._myboard[(row*self._gridsize)+col+1] = self._realboard[(row*self._gridsize)+col+1]
                    self.recursive_all_zeros(row, col+1)

    def zeroed(self):
        zeroes = []
        #print("HUH+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for i in range(self._gridsize*self._gridsize):
            if self.realboard[i] == 0:
                zeroes.append(i)
        #print(zeroes)
        self.first = False
        zero_tile = random.choice(zeroes)
        return (zero_tile//self._gridsize, zero_tile%self._gridsize)
        
    @property
    def observation(self):
        return self._myboard

    @observation.setter
    def observation(self, theboard):
        self._myboard = theboard
        #self._size = value.shape[0]
        return

    @property
    def myboard(self):
        return self._myboard
        
    def first(self):
        return self._first

    @property
    def gridsize(self):
        return self._gridsize
    
    @property
    def minecount(self):
        return self._minecount
    @property
    def realboard(self):
        return self._realboard


    def __str__(self):
        board = self.formatbothboards() #shows unmasked board and masked board - useful for debugging
        #board = self.formatfullboard #shows unmasked board only
        #board = self.formatplayerboard() #shows masked board only
        return board


    def formatbothboards(self):
        board = "\n    "
        for col in range(self._gridsize): #column index numbers
            if len(str(col)) >= 2:
                board += " "+ str(col) +" "
            else:
                board += "  "+ str(col) +" "
        board = board + "  " + "  " + "  "
        for col in range(self._gridsize): #column index numbers
            if len(str(col)) >= 2:
                board += " "+ str(col) +" "
            else:
                board += "  "+ str(col) +" "
        board += "\n    "
        for _ in range(self._gridsize): #top line
            board += "----"
        board = board + "- " + "  " + "  "
        for _ in range(self._gridsize): #top line
            board += "----"
        board += "-\n"
        #start of actual board values
        for row in range(self._gridsize): #row index numbers
            if len(str(row)) >= 2:
                board += " "+ str(row) +" "
            else:
                board += "  "+ str(row) +" "
            for col in range(self._gridsize): #column
                if self._realboard[(row * self._gridsize)+col] == -1: #mine
                    board += "| " + "M" + " "
                else:
                    board += "| " + str(self._realboard[(row * self._gridsize)+col]) + " "
            board += "| "
            if len(str(row)) >= 2:
                board += " "+ str(row) +" "
            else:
                board += "  "+ str(row) +" "
            for col in range(self._gridsize): #column
                if self._myboard[(row * self._gridsize)+col] == -2: #flagged
                    board += "| " + "F" + " "
                elif self._myboard[(row * self._gridsize)+col] == -3: #blank
                    board += "|   "
                    #board += "| " + str(self._myboard[(row * self._gridsize)+col]) + " "
                elif self._myboard[(row * self._gridsize)+col] == -1: #fmine has been triggered
                    board += "| " + "X" + " "
                else:
                    board += "| " + str(self._myboard[(row * self._gridsize)+col]) + " "

            board += "|\n    "
            for _ in range(self._gridsize): #bottom line
                board += "----"
            board = board + "- " + "  " + "  "
            for _ in range(self._gridsize): #bottom line
                board += "----"
            board += "-\n"
        return board

    def formatplayerboard(self):
        #board the user sees
        board = "\n    "
        for col in range(self._gridsize): #column index numbers
            if len(str(col)) >= 2:
                board += " "+ str(col) +" "
            else:
                board += "  "+ str(col) +" "
        board += "\n    "
        for _ in range(self._gridsize): #top line
            board += "----"
        board += "-\n"
        #start of actual board values
        for row in range(self._gridsize): #row index numbers
            if len(str(row)) >= 2:
                board += " "+ str(row) +" "
            else:
                board += "  "+ str(row) +" "
            for col in range(self._gridsize): #column
                if self._myboard[(row * self._gridsize)+col] == -2: #flagged
                    board += "| " + "F" + " "
                elif self._myboard[(row * self._gridsize)+col] == -3: #blank
                    board += "|   "
                elif self._myboard[(row * self._gridsize)+col] == -1: #fmine has been triggered
                    board += "| " + "X" + " "
                    #board += "| " + str(self._myboard[(row * self._gridsize)+col]) + " "
                else:
                    board += "| " + str(self._myboard[(row * self._gridsize)+col]) + " "
            board += "|\n    "
            for _ in range(self._gridsize): #bottom line
                board += "----"
            board += "-\n"
        return board

    def formatfullboard(self):
        #Unmasked board
        board = "\n    "
        for col in range(self._gridsize): #column index numbers
            if len(str(col)) >= 2:
                board += " "+ str(col) +" "
            else:
                board += "  "+ str(col) +" "
        board += "\n    "
        for _ in range(self._gridsize): #top line
            board += "----"
        board += "-\n"
        #start of actual board values
        for row in range(self._gridsize): #row index numbers
            if len(str(row)) >= 2:
                board += " "+ str(row) +" "
            else:
                board += "  "+ str(row) +" "
            for col in range(self._gridsize): #column
                if self._realboard[(row * self._gridsize)+col] == -1: #mine
                    board += "| " + "M" + " "
                else:
                    board += "| " + str(self._realboard[(row * self._gridsize)+col]) + " "
            board += "|\n    "
            for _ in range(self._gridsize): #bottom line
                board += "----"
            board += "-\n"
        return board
    
class MinesweeperModel:

    '''def ACTIONS(state): # row, col, choice = action
        actions = []
        for a in range(3):
            for r in range(state.gridsize):
                for c in range(state.gridsize):
                    choice = (r,c,a)
                    actions.append(choice)
        return actions'''

    def RESULT(state, action): 
        state1 = copy.deepcopy(state)
        state1.turn(action)
        return state1

    def LOSS_TEST(state):
        for i in range(state.gridsize*state.gridsize):
            if state.myboard[i] == -1:
                #print("KABOOM!!! You got blown up!")
                print("0")
                return True
            #elif state.myboard[i] == -2 and state.realboard[i] != -1:
                #print("Flag in bad spot!")
                #print("2")
                #return True
        return False

    def GOAL_TEST(state):
        flags_correct = 0
        flags_placed = 0
        for i in range(state.gridsize*state.gridsize):
            if state.myboard[i] == -2:
                if state.realboard[i] == -1: #flag is correct
                    flags_placed += 1
                    flags_correct += 1
                else: #flag is incorrect
                    flags_placed += 1
        if flags_correct == state.minecount and flags_placed == state.minecount:
            #print("All mines flagged - YOU WIN")
            print("1")
            return True
        else:
            return False


    def STEP_COST(state, action, state1):
        row, col, choice = action
        i = row*state.gridsize + col
        if choice == 0 and state.myboard[i] != -3: #click where board is not blank
            return -1
        elif choice == 1 and state.myboard[i] != -3: #flag where board is not blank
            return -1
        elif choice == 2 and state.myboard[i] != -2: #unflag where no flag exists
            return -1  
        else:
            return 0

    def FINAL_COST(state):
        flags_placed = 0
        reward = 0
        for i in range(state.gridsize*state.gridsize):
            #if state.myboard[i] == -1: #mine has been detonated
                #reward -= state.gridsize*state.gridsize
            if state.realboard[i] == -1:
                if state.myboard[i] == -2: #mine is correctly flagged
                    flags_placed+=1
                    reward += 1
            elif state.myboard[i] == -2 and state.realboard[i] != -1: #flag is incorrect
                reward -= 1
                flags_placed-=1
        if flags_placed == state.minecount:
            reward = state.gridsize*state.gridsize
        return reward




    '''def HEURISTIC(state):
        estimated_cost = 0.0
        return estimated_cost'''



    
