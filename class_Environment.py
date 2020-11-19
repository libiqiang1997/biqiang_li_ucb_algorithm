import numpy as np
from class_Arm import Arm


class Environment(object):
    def __init__(self, k, sigma_noise):
        self.k = k
        self.sigma_noise = sigma_noise

        self.unif_min = -1
        self.unif_max = 1
        # self.re_init()

    def re_init(self):
        self.expected_rewards = np.random.uniform(self.unif_min, self.unif_max, self.k)
        self.arms = []
        for i in range(self.k):
            arm_id = i
            # if arm_id == 0:
            #     arm_feature = np.array([-0.97751318, 0.23880845, -0.69363587, 0.27505283, 0.23246979])
            # else:
            #     arm_feature = np.array([0.59011134, 0.04635786, -0.58742907, -0.55982136, 0.9851805])
            # arm_feature = np.array([1, 1, 1, 1, 1])
            arm_expected_reward = self.expected_rewards[i]
            self.arms.append(Arm(arm_id, arm_expected_reward))
        # print('self.expected_rewards:', self.expected_rewards)
        # for arm in self.arms:
        #     print('arm.arm_expected_reward：', arm.arm_expected_reward)

    def play(self, choice):
        # print('arm_id:', self.arms[choice].arm_id)
        # print('arm_expected_reward:', self.arms[choice].arm_expected_reward)
        reward = self.arms[choice].pull(self.sigma_noise)
        return reward

    def get_expected_reward(self, choice):
        # print('self.expected_rewards:', self.expected_rewards)
        expected_reward = self.expected_rewards[choice]
        return expected_reward

    def get_optimal_expected_reward(self):
        optimal_expected_reward = np.max(self.expected_rewards)
        return optimal_expected_reward


# k = 10
# sigma_noise = 1
# environment = Environment(k, sigma_noise)
# environment.re_init()
