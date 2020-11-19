import numpy as np


class Arm(object):
    def __init__(self, arm_id, arm_expected_reward):
        self.arm_id = arm_id
        self.arm_expected_reward = arm_expected_reward

    def pull(self, sigma_noise):
        reward = np.random.normal(self.arm_expected_reward, sigma_noise)
        return reward