import gym
import pygame
import playplot
from gym.utils.play import play
mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 1}
play(gym.make("CartPole-v0"), keys_to_action=mapping)

def callback(obs_t, obs_tp1, action, rew, done, info):
    return [rew,]
plotter = PlayPlot(callback, 30 * 5, ["reward"])
env = gym.make("Pong-v0")
play(env, callback=plotter.callback)