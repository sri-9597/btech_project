import gym
import gym.utils.play as gp
# import numpy as np
# import time
# import keyboard

def callback(prev_obs, obs, action, rew, env_done, info):
    if not env_done:
        data_tuple = (prev_obs,obs,action,rew)
        game_data.append(data_tuple)


game_data = list()
gp.play(gym.make('BreakoutNoFrameskip-v4'),fps=20,zoom=3,callback=callback)



# exit()
# env = gym.make('BreakoutNoFrameskip-v4')
# for episode in range(10):
#     print("Episode" + str(episode) + "Done")
#     env.reset()
#     for _ in range(1000):
#         env.render(mode='human')
#         action = 0
#         if keyboard.is_pressed('s'):
#             action = 1
#         elif keyboard.is_pressed('a'):
#             action = 3
#         elif keyboard.is_pressed('d'):
#             action = 2
#         observation, reward, done, info = env.step(action)
#         # time.sleep(0.2)
#         if done:
#             break
#         print(reward)