#!/usr/bin/env python3
from gamehelper import AgentHelper
import gymnasium as gym
import mine_sweeper
import random
import time

def agent_function(state, helper):
    gridsize = state._gridsize
    myboard = state.myboard
    action_list = [] #(slot, action)
    all_unsearched = []
    pattern121right = helper.pattern_1_2_X_right(myboard)
    if pattern121right[0] != -5:
        print("Pattern 1-2-X going to the right")
        return (pattern121right[0], pattern121right[1], 1)
    pattern121left = helper.pattern_1_2_X_left(myboard)
    if pattern121left[0] != -5:
        print("Pattern 1-2-X going to the left")
        return (pattern121left[0], pattern121left[1], 1)
    pattern121down = helper.pattern_1_2_X_down(myboard)
    if pattern121down[0] != -5:
        print("Pattern 1-2-X going down")
        return (pattern121down[0], pattern121down[1], 1)
    pattern121up = helper.pattern_1_2_X_up(myboard)
    if pattern121up[0] != -5:
        print("Pattern 1-2-X going up")
        return (pattern121up[0], pattern121up[1], 1)
    q1actions, q1unsearched = helper.q1_of_neighbors(myboard)
    if len(q1actions) != 0:
        action = random.choice(q1actions)
        print("q1 choice")
        return (action[0]//gridsize, action[0]%gridsize, action[1])
    all_unsearched += q1unsearched
    q2actions, q2unsearched = helper.q2_of_neighbors(myboard)
    if len(q2actions) != 0:
        print("q2 choice")
        action = random.choice(q2actions)
        return (action[0]//gridsize, action[0]%gridsize, action[1])
    all_unsearched += q2unsearched
    q3actions, q3unsearched = helper.q3_of_neighbors(myboard)
    if len(q3actions) != 0:
        print("q3 choice")
        action = random.choice(q3actions)
        return (action[0]//gridsize, action[0]%gridsize, action[1])
    all_unsearched += q3unsearched
    q4actions, q4unsearched = helper.q4_of_neighbors(myboard)
    if len(q4actions) != 0:
        print("q4 choice")
        action = random.choice(q4actions)
        return (action[0]//gridsize, action[0]%gridsize, action[1])
    all_unsearched += q4unsearched
    action = random.choice(all_unsearched)
    print("Random choice")
    return (action[0]//gridsize, action[0]%gridsize, 0)



def data_agent_function(state, helper):
    gridsize = state._gridsize
    myboard = state.myboard
    action_list = [] #(slot, action)
    all_unsearched = []
    #search by quarters 
    q1actions, q1unsearched = helper.q1_of_neighbors(myboard)
    if len(q1actions) != 0:
        print("0")
        action = random.choice(q1actions)
        return (action[0]//gridsize, action[0]%gridsize, action[1])
    all_unsearched += q1unsearched

    q2actions, q2unsearched = helper.q2_of_neighbors(myboard)
    if len(q2actions) != 0:
        print("0")
        action = random.choice(q2actions)
        return (action[0]//gridsize, action[0]%gridsize, action[1])
    all_unsearched += q2unsearched

    q3actions, q3unsearched = helper.q3_of_neighbors(myboard)
    if len(q3actions) != 0:
        print("0")
        action = random.choice(q3actions)
        return (action[0]//gridsize, action[0]%gridsize, action[1])
    all_unsearched += q3unsearched

    q4actions, q4unsearched = helper.q4_of_neighbors(myboard)
    if len(q4actions) != 0:
        print("0")
        action = random.choice(q4actions)
        return (action[0]//gridsize, action[0]%gridsize, action[1])
    all_unsearched += q4unsearched

    pattern121right = helper.pattern_1_2_X_right(myboard)
    if pattern121right[0] != -5:
        print("1")
        return (pattern121right[0], pattern121right[1], 1)

    pattern121left = helper.pattern_1_2_X_left(myboard)
    if pattern121left[0] != -5:
        print("1")
        return (pattern121left[0], pattern121left[1], 1)

    pattern121down = helper.pattern_1_2_X_down(myboard)
    if pattern121down[0] != -5:
        print("1")
        return (pattern121down[0], pattern121down[1], 1)

    pattern121up = helper.pattern_1_2_X_up(myboard)
    if pattern121up[0] != -5:
        print("1")
        return (pattern121up[0], pattern121up[1], 1)

    action = random.choice(all_unsearched)
    print("2")
    return (action[0]//gridsize, action[0]%gridsize, 0)


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
    env = gym.make('mine_sweeper/MineSweeper-v0', render_mode=render_mode, grid_size=grid_size, mine_count=mine_count, max_episode_steps=(grid_size*grid_size)+1)
    observation, info = env.reset()
    state = mine_sweeper.MinesweeperState(grid_size, mine_count)  
    terminated = truncated = False
    if zeroed == "y":
        zrow, zcol = info["zero"]
        observation, reward, terminated, truncated, info = env.step((zrow, zcol, 0))
        state.observation = observation
        if render_mode == "ansi":
            print("Current state:", env.render())
    helper = AgentHelper(grid_size)
    start_time = time.time()
    while not (terminated or truncated):
        action = data_agent_function(state, helper)
        #action = agent_function(state, helper)
        row, col, act = action  
        observation, reward, terminated, truncated, info = env.step(action)
        state.observation = observation
        if render_mode == "ansi":
            print(f"{action_options[act]} {row, col}")
            print("Current state:", env.render())
    end_time = time.time()        
    env.close()
    #if reward > grid_size*grid_size:
        #penalty = reward-grid_size*grid_size
        #reward = grid_size*grid_size - penalty
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
    
    


