import os
path_strs = os.getcwd().split('\\')
current_dir_name = path_strs[len(path_strs)-1]
jupyter_notebook = False
if current_dir_name == 'jupyter_notebook':
    jupyter_notebook = True
    os.chdir("..")
from class_Environment import Environment
from class_Simulator import Simulator
from algorithm_class.class_UCB import UCB
from util import plot_regret, modify_regret_figure, plot_supplementary_figure
from datetime import datetime


def run_experiment(num_mc, option):
    bandit_env = Environment(k, sigma_noise)
    simulator = Simulator(bandit_env, policies)
    if option == 'solo_processing':
        avg_regret = simulator.run(num_mc, time_horizon)
        return avg_regret
    elif option == 'multi_processing':
        avg_regret = simulator.multiprocessing_run(num_thread, num_mc, time_horizon)
        return avg_regret


time_horizon = 5000
k = 10
delta = 0.01
num_mc = 100
line_name = 'UCB'


def solo_processing():
    # solo_processing
    option = 'solo_processing'
    sigma_noise = 0.1
    figure_name = ('ucb_convergence_verification_sigma' + str(sigma_noise)).replace('.', 'dot')
    policies = [UCB(sigma_noise, k, delta)]
    avg_regret = run_experiment(num_mc, option)
    plot_regret(figure_name, line_name, avg_regret, jupyter_notebook)


def multi_processing():
    global num_thread, sigma_noise, policies
    # multi_processing
    option = 'multi_processing'
    num_thread = 10
    sigma_noise = 0.1
    figure_name = ('ucb_convergence_verification_sigma' + str(sigma_noise)).replace('.', 'dot')
    policies = [UCB(sigma_noise, k, delta)]
    avg_regret = run_experiment(num_mc, option)
    plot_regret(figure_name, line_name, avg_regret, jupyter_notebook)


def modify_figure():
    # modify_figure
    figure_name = 'ucb_convergence_verification_sigma1'
    modify_regret_figure(figure_name, line_name, jupyter_notebook)


if __name__ == '__main__':
    start_time = datetime.now()

    solo_processing()
    # multi_processing()
    # modify_figure()
    # plot_supplementary_figure()

    end_time = datetime.now()
    cost_time = end_time - start_time
    print('start_time:', start_time)
    print('end_time:', end_time)
    print('cost_time:', cost_time)