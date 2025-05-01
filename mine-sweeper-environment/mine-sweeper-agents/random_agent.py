#!/usr/bin/env python3
import time
import gymnasium as gym
import mine_sweeper
import random

def agent_function(state, grid_size):
    """
    state: A uniform_coins.UniformCoinsState object. The current state of the environment.
    
    returns: An integer, the coin to turn over.
    """
    row = random.randint(0, grid_size-1)
    col = random.randint(0, grid_size-1)
    pick = random.randint(0, 1)
    action = (row, col, pick)
    #action = random.choice(mine_sweeper.MinesweeperModel.ACTIONS(state))
    return action

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
    steps = grid_size*grid_size
    env = gym.make('mine_sweeper/MineSweeper-v0', render_mode=render_mode, grid_size=grid_size, mine_count=mine_count, max_episode_steps=steps)
    observation, info = env.reset()
    state = mine_sweeper.MinesweeperState(grid_size, mine_count)
    state.observation = observation
    terminated = truncated = False
    if zeroed == "y":
        zrow, zcol = info["zero"]
        observation, reward, terminated, truncated, info = env.step((zrow, zcol, 0))
        state.observation = observation
        if render_mode == "ansi":
            print("Current state:", env.render())
    start_time = time.time()
    while not (terminated or truncated):
        #action = data_agent_function(state, helper)
        action = agent_function(state, grid_size)
        row, col, act = action  
        observation, reward, terminated, truncated, info = env.step(action)
        state.observation = observation
        if render_mode == "ansi":
            print(f"{action_options[act]} {row, col}")
            print("Current state:", env.render())
    end_time = time.time()        
    env.close()
    if reward > grid_size*grid_size:
        penalty = reward-grid_size*grid_size
        reward = grid_size*grid_size - penalty
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
    
    


