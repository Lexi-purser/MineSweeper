from gymnasium.envs.registration import register

from mine_sweeper.envs.mine_sweeper_env import MineSweeperEnv
from mine_sweeper.envs.mine_sweeper_model import MinesweeperModel
from mine_sweeper.envs.mine_sweeper_model import MinesweeperState

register(
    id="mine_sweeper/MineSweeper-v0",
    entry_point="mine_sweeper.envs:MineSweeperEnv",
    max_episode_steps=500,
)