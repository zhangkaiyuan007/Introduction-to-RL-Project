# Part 1
import gymnasium as gym
from time import sleep

env = gym.make('CartPole-v1', render_mode='human')
state, _ = env.reset()
# Watch random actions
for _ in range(1000):
    action = env.action_space.sample()  # Random action
    state, reward, terminated, truncated, _ = env.step(action)
    if terminated or truncated:
        print('The cartpole has tipped over!')
        sleep(2)
        state, _ = env.reset()
env.close()