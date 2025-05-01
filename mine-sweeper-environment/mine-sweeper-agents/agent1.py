#!/usr/bin/env python3

import gymnasium as gym
import mine_sweeper
import random
import time

#blank = -3     flagged = -2
def agent_function(state):
    #print(state)
    gridsize = state._gridsize
    myboard = state.myboard
    #print(myboard)
    action_list = [] #(slot, action)
    all_unsearched = []
    for slot in range(gridsize*gridsize):
        if slot > gridsize*gridsize-1: continue
        if myboard[slot] == -3:
            all_unsearched.append((slot, 0))
        unsearched_tally = 0
        searched_tally = 0
        flag_tally = 0
        col = slot % gridsize
        row = slot // gridsize
        unsearched_list = []
        if row > 0: #[slot-gridsize]     we can check up
            if myboard[slot-gridsize] == -3: 
                unsearched_tally+=1
                unsearched_list.append(slot-gridsize)
            elif myboard[slot-gridsize] == -2: flag_tally+=1
            else: searched_tally+=1 

        if col > 0: #[slot-1]   we can check left
            if myboard[slot-1] == -3: 
                unsearched_tally+=1
                unsearched_list.append(slot-1)
            elif myboard[slot-1] == -2: flag_tally+=1
            else: searched_tally+=1 

        if row < gridsize-1: #[slot+gridsize]    we can check down
            if myboard[slot+gridsize] == -3: 
                unsearched_tally+=1
                unsearched_list.append(slot+gridsize)
            elif myboard[slot+gridsize] == -2: flag_tally+=1
            else: searched_tally+=1 

        if col < gridsize-1: #[slot+1]  we can check right
            if myboard[slot+1] == -3: 
                unsearched_tally+=1
                unsearched_list.append(slot+1)
            elif myboard[slot+1] == -2: flag_tally+=1
            else: searched_tally+=1 

        if row > 0 and col > 0: #[slot-gridsize-1]    we can check upleft
            if myboard[slot-gridsize-1] == -3: 
                unsearched_tally+=1
                unsearched_list.append(slot-gridsize-1)
            elif myboard[slot-gridsize-1] == -2: flag_tally+=1
            else: searched_tally+=1 

        if row > 0 and col < gridsize-1: #[slot-gridsize+1]   we can check upright
            if myboard[slot-gridsize+1] == -3: 
                unsearched_tally+=1
                unsearched_list.append(slot-gridsize+1)
            elif myboard[slot-gridsize+1] == -2: flag_tally+=1
            else: searched_tally+=1 

        if row < gridsize-1 and col > 0: #[slot+gridsize-1]  we can check downleft
            if myboard[slot+gridsize-1] == -3: 
                unsearched_tally+=1
                unsearched_list.append(slot+gridsize-1)
            elif myboard[slot+gridsize-1] == -2: flag_tally+=1
            else: searched_tally+=1 

        if row < gridsize-1 and col < gridsize-1: #[slot+gridsize+1]  we can check downright
            if myboard[slot+gridsize+1] == -3: 
                unsearched_tally+=1
                unsearched_list.append(slot+gridsize+1)
            elif myboard[slot+gridsize+1] == -2: flag_tally+=1
            else: searched_tally+=1 
        if flag_tally+unsearched_tally == myboard[slot] and flag_tally != myboard[slot]:
            for opt in unsearched_list:
                action_list.append((opt, 1))
        if flag_tally == myboard[slot]:
            for opt in unsearched_list:
                action_list.append((opt, 0))
    #print(action_list)
    #print(all_unsearched)
    if len(action_list) == 0:
        action =  random.choice(all_unsearched)
    else:
        action = random.choice(action_list)
    col = action[0] % gridsize
    row = action[0] // gridsize
    return (row, col, action[1])


def patterns(state):
    d






def main(level, zeroed, render):
    board_sizes = { 0 : (9,10), 1 : (16,40), 2 : (22, 99)}
    grid_size = board_sizes[level][0]
    mine_count = board_sizes[level][1]
    # 0 = click, 1 = flag, 2 = remove flag
    action_options = {0 : "Click", 1 : "Flag", 2 : "Remove Flag"}
    if render == "y":
        render_mode = "ansi"
    else:
        render_mode = None
    env = gym.make('mine_sweeper/MineSweeper-v0', render_mode=render_mode, grid_size=grid_size, mine_count=mine_count, max_episode_steps=500)
    observation, info = env.reset()
    state = mine_sweeper.MinesweeperState(grid_size, mine_count)
    #print(info["zero"])
    #print(state)
    state.observation = observation
    terminated = truncated = False
    #reward = 0
    if zeroed == "y":
        zrow, zcol = info["zero"]
        action = (zrow, zcol, 0)
        observation, reward, terminated, truncated, info = env.step(action)
        state.observation = observation
        if render_mode == "ansi":
            print("Current state:", env.render())
    start_time = time.time()
    while not (terminated or truncated):
        action = agent_function(state)
        row, col, act = action  
        observation, reward, terminated, truncated, info = env.step(action)
        state.observation = observation
        if render_mode == "ansi":
            print(f"{action_options[act]} {row, col}")
            print("Current state:", env.render())
    #print("------Game Terminated------")
    env.close()
    end_time = time.time()
    print(reward,end_time-start_time, sep=",")
    return





if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "level",
        type=int,
        help="board option\n0 - 9x9 board with 10 mines\n1 - 16x16 board with 40 mines\n2 - 21x21 board with 99 mines",
        choices=[0,1,2],
        default=0,
    )
    parser.add_argument(
        "zeroed",
        type=str,
        help="First choice is automaticaly done on a zero tile",
        choices=["y", "n"],
        default="n",
    )

    parser.add_argument(
        "render",
        type=str,
        help="Render game graphics",
        choices=["y", "n"],
        default="n",
    )

    args = parser.parse_args()
    main(args.level, args.zeroed, args.render)
    
    


