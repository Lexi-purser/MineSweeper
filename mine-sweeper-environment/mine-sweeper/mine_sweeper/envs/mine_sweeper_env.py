import gymnasium
import numpy as np
from gymnasium import spaces
from mine_sweeper.envs.mine_sweeper_model import MinesweeperModel
from mine_sweeper.envs.mine_sweeper_model import MinesweeperState

try:
    import pygame
except ImportError as e:
    raise DependencyNotInstalled(
        "pygame is not installed, `pip install` must have failed."
    ) from e

class MineSweeperEnv(gymnasium.Env):
    
    metadata = {
        "render_modes": ["human", "rgb_array", "ansi"],
        "render_fps": 1,
    }
    
    def __init__(self, render_mode, grid_size, mine_count):
        self.step_count = 0
        self.reward = 0
        self.render_mode = render_mode
        self.grid_size = grid_size #ex: grid_size is 8 then board is 8x8
        self.mine_count = mine_count #number of mines on the board
        self.action_space = spaces.Discrete(3) # 0 = click, 1 = flag, 2 = remove flag
        self.observation_space = spaces.Box(-3, 99, shape=(grid_size*grid_size,), dtype=np.int64)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = MinesweeperState(self.grid_size, self.mine_count)
        self.state.randomize()

        observation = self.state.observation
        z = self.state.zeroed()
        info = {"zero": z}
        return observation, info

    def step(self, action):
        self.step_count += 1
        state = self.state
        state1 = MinesweeperModel.RESULT(state, action)
        self.state = state1
        
        observation = self.state.observation
        self.reward += MinesweeperModel.STEP_COST(state, action, state1)
        if MinesweeperModel.LOSS_TEST(state1) == True:
            terminated = True
        else:
            terminated = MinesweeperModel.GOAL_TEST(state1)
        info = {} #"steps" : self.step_count
        if terminated or self.step_count == self.grid_size*self.grid_size: 
            if self.step_count == self.grid_size*self.grid_size: 
                self.reward -= self.grid_size*self.grid_size
            self.reward += MinesweeperModel.FINAL_COST(state1)
            #print("Final step count: ", self.step_count)
        # display support
        if self.render_mode == "human":
            self.render()
        return observation, self.reward, terminated, False, info

    def render(self):
        return str(self.state)




    
