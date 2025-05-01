
class AgentHelper:

    def __init__(self, gridsize):
        self.gridsize = gridsize
        self.fullsize = gridsize*gridsize
        self.myboard = []

    def pattern_1_2_X_right(self, myboard):
        self.myboard = myboard
        for row in range(self.gridsize):
            for col in range(self.gridsize-1):
                slot = row*self.gridsize + col
                if myboard[slot] == 1 and (self.right(slot)) and (self.get_right(slot)) == 2 and (self.right(slot+1)) and (self.get_right(slot+1)) != -2 and (self.get_right(slot+1)) != -3:
                    #possible 1-2-X pattern
                    if row == 0 or (self.up(slot)) and (self.get_up(slot)) != -2 and (self.get_up(slot)) != -3 and (self.upright(slot)) and (self.get_upright(slot)) != -2 and (self.get_upright(slot)) != -3 and (self.upright(slot+1)) and (self.get_upright(slot+1)) != -2 and (self.get_upright(slot+1)) != -3:
                        #up is searched or we are on the top row (row 0)
                        if  col == 0 or (self.upleft(slot)) and (self.get_upleft(slot)) != -2 and (self.get_upleft(slot)) != -3 and (self.get_left(slot)) != -2 and (self.get_left(slot)) != -3: 
                            if (self.downright(slot)) and self.get_downright(slot) == -3 or col == 0:
                                if self.down(slot) and self.get_down(slot) == -3 and self.downright(slot) and self.get_downright(slot) == -3 and self.downright(slot+1) and self.get_downright(slot+1) == -3:
                                    #down is unflagged blanks
                                    return row+1, col+2
                    elif row == 0 or (self.down(slot)) and (self.get_down(slot)) != -2 and (self.get_down(slot)) != -3 and (self.downright(slot)) and (self.get_downright(slot)) != -2 and (self.get_downright(slot)) != -3 and (self.downright(slot+1)) and (self.get_downright(slot+1)) != -2 and (self.get_downright(slot+1)) != -3:
                        #down is seached or we are on the bottom row (row gridsize-1)
                        if  col == 0 or (self.downleft(slot)) and (self.get_downleft(slot)) != -2 and (self.get_left(slot)) and (self.get_left(slot)) != -2 and (self.get_left(slot)) != -3: 
                            if (self.upright(slot)) and self.get_upright(slot) == -3 or col == 0:
                                if self.up(slot) and self.get_up(slot) == -3 and self.upright(slot+1) and self.get_upright(slot+1) == -3:
                                    #up is unflagged blanks
                                    return row-1, col+2

        return -5, 0

    def pattern_1_2_X_left(self, myboard):
        self.myboard = myboard
        for row in range(self.gridsize):
            for col in range(self.gridsize-1, -1, -1):
                slot = row*self.gridsize + col
                if myboard[slot] == 1 and (self.left(slot)) and (self.get_left(slot)) == 2 and (self.left(slot-1)) and (self.get_left(slot-1)) != -2 and (self.get_left(slot-1)) != -3:
                    if row == 0 or (self.up(slot)) and (self.get_up(slot)) != -2 and (self.get_up(slot)) != -3 and (self.upleft(slot)) and (self.get_upleft(slot)) != -2 and (self.get_upleft(slot)) != -3 and (self.upleft(slot-1)) and (self.get_upleft(slot-1)) != -2 and (self.get_upleft(slot-1)) != -3 and (self.upright(slot)) and (self.get_upright(slot)) != -2 and (self.get_upright(slot)) != -3: 
                        if (self.down(slot)) and (self.get_down(slot)) == -3 and (self.downleft(slot)) and (self.get_downleft(slot)) == -3 and (self.downleft(slot-1)) and (self.get_downleft(slot-1)) == -3:
                            return row+1, col-2
                    elif row == self.gridsize-1 or (self.down(slot)) and (self.get_down(slot)) != -2 and (self.get_down(slot)) != -3 and (self.downleft(slot)) and (self.get_downleft(slot)) != -2 and (self.get_downleft(slot)) != -3 and (self.downleft(slot-1)) and (self.get_downleft(slot-1)) != -2 and (self.get_downleft(slot-1)) != -3:
                        if row == self.gridsize-1 or (self.downright(slot)) and (self.get_downright(slot)) != -2 and (self.get_downright(slot)) != -3: 
                            if (self.up(slot)) and (self.get_up(slot)) == -3 and (self.upleft(slot)) and (self.get_upleft(slot)) == -3 and (self.upleft(slot-1)) and (self.get_upleft(slot-1)) == -3:
                                return row-1, col-2
        return -5, 0


    def pattern_1_2_X_down(self, myboard):
        for col in range(self.gridsize):
            for row in range(self.gridsize):
                slot = row*self.gridsize + col
                if myboard[slot] == 1 and (self.up(slot)) and (self.get_up(slot)) != -2 and (self.get_up(slot)) != -3 and (self.down(slot)) and (self.get_down(slot)) == 2 and (self.down(slot+self.gridsize)) and (self.get_down(slot+self.gridsize)) != -2 and (self.get_down(slot+self.gridsize)) != -3:
                    if (self.upleft(slot)) and (self.downleft(slot+self.gridsize)) and (self.get_upleft(slot)) == -3 and (self.get_left(slot)) == -3  and (self.get_downleft(slot)) == -3  and (self.get_downleft(slot+self.gridsize)) == -3:
                        if col == self.gridsize-1 or (self.upright(slot)) and (self.downright(slot+self.gridsize)) and (self.get_upright(slot)) != -2 and (self.get_upright(slot)) != -3 and (self.get_right(slot)) != -2 and (self.get_right(slot)) != -3 and (self.get_downright(slot)) != -2 and (self.get_downright(slot)) != -3 and (self.get_downright(slot+self.gridsize)) != -2 and (self.get_downright(slot+self.gridsize)) != -3:
                            return row+2, col-1
                    elif (self.upright(slot)) and (self.downright(slot+self.gridsize)) and (self.get_upright(slot)) == -3 and (self.get_right(slot)) == -3  and (self.get_downright(slot)) == -3  and (self.get_downright(slot+self.gridsize)) == -3:
                        if col == 0 or (self.upleft(slot)) and (self.downleft(slot+self.gridsize)) and (self.get_upleft(slot)) != -2 and (self.get_upleft(slot)) != -3 and (self.get_left(slot)) != -2 and (self.get_left(slot)) != -3 and (self.get_downleft(slot)) != -2 and (self.get_downleft(slot)) != -3 and (self.get_downleft(slot+self.gridsize)) != -2 and (self.get_downleft(slot+self.gridsize)) != -3:
                            return row+2, col+1
        return -5, 0


    def pattern_1_2_X_up(self, myboard):
        for col in range(self.gridsize):
            for row in range(self.gridsize-1,-1,-1):
                slot = row*self.gridsize + col
                if myboard[slot] == 1 and (self.down(slot)) and (self.get_down(slot)) != -2 and (self.get_down(slot)) != -3 and (self.up(slot)) and (self.get_up(slot)) == 2 and (self.up(slot-self.gridsize)) and (self.get_up(slot-self.gridsize)) != -2 and (self.get_up(slot-self.gridsize)) != -3:
                    if (self.downleft(slot)) and (self.upleft(slot-self.gridsize)) and (self.get_downleft(slot)) == -3 and (self.get_left(slot)) == -3  and (self.get_upleft(slot)) == -3  and (self.get_upleft(slot-self.gridsize)) == -3:
                        if col == self.gridsize-1 or (self.downright(slot)) and (self.upright(slot-self.gridsize)) and (self.get_downright(slot)) != -2 and (self.get_downright(slot)) != -3 and (self.get_right(slot)) != -2 and (self.get_right(slot)) != -3 and (self.get_upright(slot)) != -2 and (self.get_upright(slot)) != -3 and (self.get_upright(slot-self.gridsize)) != -2 and (self.get_upright(slot-self.gridsize)) != -3:
                            return row-2, col-1
                    elif (self.downright(slot)) and (self.upright(slot-self.gridsize)) and (self.get_downright(slot)) == -3 and (self.get_right(slot)) == -3  and (self.get_upright(slot)) == -3  and (self.get_upright(slot-self.gridsize)) == -3:
                        if col == 0 or (self.downleft(slot)) and (self.upleft(slot-self.gridsize)) and (self.get_downleft(slot)) != -2 and (self.get_downleft(slot)) != -3 and (self.get_left(slot)) != -2 and (self.get_left(slot)) != -3 and (self.get_upleft(slot)) != -2 and (self.get_upleft(slot)) != -3 and (self.get_upleft(slot-self.gridsize)) != -2 and (self.get_upleft(slot-self.gridsize)) != -3:
                            return row-2, col+1
        return -5, 0



    def q1_of_neighbors(self, myboard):
        self.myboard = myboard
        action_list = []
        second_action_list = []
        unsearched = []
        for slot in range(int(self.fullsize/4)):
            #if slot >= self.fullsize: continue
            if myboard[slot] == -3: 
                unsearched.append((slot, 0))
                continue
            unsearched_tally = 0
            flag_tally = 0
            unsearched_list = []
            if (self.up(slot)):
                if (self.get_up(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append((self.up_slot(slot)))
                elif (self.get_up(slot)) == -2: flag_tally+=1
            if (self.down(slot)): 
                if (self.get_down(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.down_slot(slot))
                elif (self.get_down(slot)) == -2: flag_tally+=1
            if (self.left(slot)):
                if (self.get_left(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.left_slot(slot))
                elif (self.get_left(slot)) == -2: flag_tally+=1
            if (self.right(slot)): 
                if (self.get_right(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.right_slot(slot))
                elif (self.get_right(slot)) == -2: flag_tally+=1
            if (self.upleft(slot)):
                if (self.get_upleft(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.upleft_slot(slot))
                elif (self.get_upleft(slot)) == -2: flag_tally+=1
            if (self.upright(slot)): 
                if (self.get_upright(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.upright_slot(slot))
                elif (self.get_upright(slot)) == -2: flag_tally+=1
            if (self.downleft(slot)):
                if (self.get_downleft(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.downleft_slot(slot))
                elif (self.get_downleft(slot)) == -2: flag_tally+=1
            if (self.downright(slot)): 
                if (self.get_downright(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.downright_slot(slot))
                elif (self.get_downright(slot)) == -2: flag_tally+=1
            if flag_tally+unsearched_tally == myboard[slot] and flag_tally != myboard[slot]:
                for opt in unsearched_list:
                    action_list.append((opt, 1))
            if flag_tally == myboard[slot]:
                for opt in unsearched_list:
                    action_list.append((opt, 0))
        return action_list, unsearched

    def q2_of_neighbors(self, myboard):
        self.myboard = myboard
        action_list = []
        second_action_list = []
        unsearched = []
        for slot in range(int(self.fullsize/4), int(self.fullsize/2)):
            #if slot >= self.fullsize: continue
            if myboard[slot] == -3: 
                unsearched.append((slot, 0))
                continue
            unsearched_tally = 0
            flag_tally = 0
            unsearched_list = []
            if (self.up(slot)):
                if (self.get_up(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append((self.up_slot(slot)))
                elif (self.get_up(slot)) == -2: flag_tally+=1
            if (self.down(slot)): 
                if (self.get_down(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.down_slot(slot))
                elif (self.get_down(slot)) == -2: flag_tally+=1
            if (self.left(slot)):
                if (self.get_left(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.left_slot(slot))
                elif (self.get_left(slot)) == -2: flag_tally+=1
            if (self.right(slot)): 
                if (self.get_right(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.right_slot(slot))
                elif (self.get_right(slot)) == -2: flag_tally+=1
            if (self.upleft(slot)):
                if (self.get_upleft(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.upleft_slot(slot))
                elif (self.get_upleft(slot)) == -2: flag_tally+=1
            if (self.upright(slot)): 
                if (self.get_upright(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.upright_slot(slot))
                elif (self.get_upright(slot)) == -2: flag_tally+=1
            if (self.downleft(slot)):
                if (self.get_downleft(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.downleft_slot(slot))
                elif (self.get_downleft(slot)) == -2: flag_tally+=1
            if (self.downright(slot)): 
                if (self.get_downright(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.downright_slot(slot))
                elif (self.get_downright(slot)) == -2: flag_tally+=1
            if flag_tally+unsearched_tally == myboard[slot] and flag_tally != myboard[slot]:
                for opt in unsearched_list:
                    action_list.append((opt, 1))
            if flag_tally == myboard[slot]:
                for opt in unsearched_list:
                    second_action_list.append((opt, 0))
        if len(action_list) != 0:
            return action_list, unsearched
        return second_action_list, unsearched


    def q3_of_neighbors(self, myboard):
        self.myboard = myboard
        action_list = []
        second_action_list = []
        unsearched = []
        for slot in range(int(self.fullsize/2), int(3*self.fullsize/4)):
            #if slot >= self.fullsize: continue
            if myboard[slot] == -3: 
                unsearched.append((slot, 0))
                continue
            unsearched_tally = 0
            flag_tally = 0
            unsearched_list = []
            if (self.up(slot)):
                if (self.get_up(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append((self.up_slot(slot)))
                elif (self.get_up(slot)) == -2: flag_tally+=1
            if (self.down(slot)): 
                if (self.get_down(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.down_slot(slot))
                elif (self.get_down(slot)) == -2: flag_tally+=1
            if (self.left(slot)):
                if (self.get_left(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.left_slot(slot))
                elif (self.get_left(slot)) == -2: flag_tally+=1
            if (self.right(slot)): 
                if (self.get_right(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.right_slot(slot))
                elif (self.get_right(slot)) == -2: flag_tally+=1
            if (self.upleft(slot)):
                if (self.get_upleft(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.upleft_slot(slot))
                elif (self.get_upleft(slot)) == -2: flag_tally+=1
            if (self.upright(slot)): 
                if (self.get_upright(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.upright_slot(slot))
                elif (self.get_upright(slot)) == -2: flag_tally+=1
            if (self.downleft(slot)):
                if (self.get_downleft(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.downleft_slot(slot))
                elif (self.get_downleft(slot)) == -2: flag_tally+=1
            if (self.downright(slot)): 
                if (self.get_downright(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.downright_slot(slot))
                elif (self.get_downright(slot)) == -2: flag_tally+=1
            if flag_tally+unsearched_tally == myboard[slot] and flag_tally != myboard[slot]:
                for opt in unsearched_list:
                    action_list.append((opt, 1))
            if flag_tally == myboard[slot]:
                for opt in unsearched_list:
                    second_action_list.append((opt, 0))
        if len(action_list) != 0:
            return action_list, unsearched
        return second_action_list, unsearched


    def q4_of_neighbors(self, myboard):
        self.myboard = myboard
        action_list = []
        second_action_list = []
        unsearched = []
        for slot in range(int(3*self.fullsize/4), self.fullsize):
            #if slot >= self.fullsize: continue
            if myboard[slot] == -3: 
                unsearched.append((slot, 0))
                continue
            unsearched_tally = 0
            flag_tally = 0
            unsearched_list = []
            if (self.up(slot)):
                if (self.get_up(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append((self.up_slot(slot)))
                elif (self.get_up(slot)) == -2: flag_tally+=1
            if (self.down(slot)): 
                if (self.get_down(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.down_slot(slot))
                elif (self.get_down(slot)) == -2: flag_tally+=1
            if (self.left(slot)):
                if (self.get_left(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.left_slot(slot))
                elif (self.get_left(slot)) == -2: flag_tally+=1
            if (self.right(slot)): 
                if (self.get_right(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.right_slot(slot))
                elif (self.get_right(slot)) == -2: flag_tally+=1
            if (self.upleft(slot)):
                if (self.get_upleft(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.upleft_slot(slot))
                elif (self.get_upleft(slot)) == -2: flag_tally+=1
            if (self.upright(slot)): 
                if (self.get_upright(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.upright_slot(slot))
                elif (self.get_upright(slot)) == -2: flag_tally+=1
            if (self.downleft(slot)):
                if (self.get_downleft(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.downleft_slot(slot))
                elif (self.get_downleft(slot)) == -2: flag_tally+=1
            if (self.downright(slot)): 
                if (self.get_downright(slot)) == -3: 
                    unsearched_tally+=1
                    unsearched_list.append(self.downright_slot(slot))
                elif (self.get_downright(slot)) == -2: flag_tally+=1
            if flag_tally+unsearched_tally == myboard[slot] and flag_tally != myboard[slot]:
                for opt in unsearched_list:
                    action_list.append((opt, 1))
            if flag_tally == myboard[slot]:
                for opt in unsearched_list:
                    second_action_list.append((opt, 0))
        if len(action_list) != 0:
            return action_list, unsearched
        return second_action_list, unsearched


    def up(self, slot):
        if slot//self.gridsize > 0: #[slot-gridsize]     we can check up
            return True
        return False

    def down(self, slot):
        if slot//self.gridsize < self.gridsize-1: #[slot+gridsize]    we can check down
            return True
        return False

    def left(self, slot):
        if slot%self.gridsize > 0: #[slot-1]   we can check left
            return True
        return False

    def right(self, slot):
        if slot%self.gridsize < self.gridsize-1: #[slot+1]  we can check right
            return True
        return False

    def upleft(self, slot):
        if slot//self.gridsize > 0 and slot%self.gridsize > 0: #[slot-gridsize-1]    we can check upleft
            return True
        return False

    def upright(self, slot):
        if slot//self.gridsize > 0 and slot%self.gridsize < self.gridsize-1: #[slot-gridsize+1]   we can check upright
            return True
        return False

    def downleft(self, slot):
        if slot//self.gridsize < self.gridsize-1 and slot%self.gridsize > 0: #[slot+gridsize-1]  we can check downleft
            return True
        return False

    def downright(self, slot):
        if slot//self.gridsize < self.gridsize-1 and slot%self.gridsize < self.gridsize-1: #[slot+gridsize+1]  we can check downright
            return True
        return False



    def get_up(self, slot):
        return self.myboard[slot-self.gridsize]

    def get_down(self, slot):
        return self.myboard[slot+self.gridsize]

    def get_left(self, slot):
        return self.myboard[slot-1]
        
    def get_right(self, slot):
        return self.myboard[slot+1]

    def get_upleft(self, slot):
        return self.myboard[slot-self.gridsize-1]

    def get_upright(self, slot):
        return self.myboard[slot-self.gridsize+1]

    def get_downleft(self, slot):
        return self.myboard[slot+self.gridsize-1]

    def get_downright(self, slot):
        return self.myboard[slot+self.gridsize+1]



    def up_slot(self, slot):
        return slot-self.gridsize

    def down_slot(self, slot):
        return slot+self.gridsize

    def left_slot(self, slot):
        return slot-1
        
    def right_slot(self, slot):
        return slot+1

    def upleft_slot(self, slot):
        return slot-self.gridsize-1

    def upright_slot(self, slot):
        return slot-self.gridsize+1

    def downleft_slot(self, slot):
        return slot+self.gridsize-1

    def downright_slot(self, slot):
        return slot+self.gridsize+1

