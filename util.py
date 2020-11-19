import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.io import loadmat
from scipy.io import savemat


# plt parameters
colors = ['black', 'red', 'green', 'blue']
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['legend.fontsize'] = 27
plt.rcParams['axes.labelsize'] = 27
# plt.rcParams['axes.labelweight'] = 'bold'
# ax = plt.gca()
# ax.xaxis.set_tick_params(labelsize=20)
plt.rcParams['xtick.labelsize'] = 27
plt.rcParams['ytick.labelsize'] = 27
plt.rcParams['figure.subplot.left'] = 0.2
plt.rcParams['figure.subplot.bottom'] = 0.17
plt.rcParams['figure.subplot.right'] = 0.96
plt.rcParams['figure.subplot.top'] = 0.99
# plt.rcParams['text.usetex'] = True
# print(plt.rcParams)

# create dir
current_path = os.getcwd()
png_path = 'output/png'
png_save_path = current_path + '/' + png_path
if not os.path.exists(png_save_path):
    os.makedirs(png_save_path)
eps_path = 'output/eps'
eps_save_path = current_path + '/' + eps_path
if not os.path.exists(eps_save_path):
    os.makedirs(eps_save_path)
mat_path = 'output/mat'
mat_save_path = current_path + '/' + mat_path
if not os.path.exists(mat_save_path):
    os.makedirs(mat_save_path)


def plot_regret(figure_name, line_name, line_regret, jupyter_notebook):
    plot_figure(line_name, line_regret)
    if not jupyter_notebook:
        save_figure(figure_name)
        save_data(figure_name, line_name, line_regret)


def modify_regret_figure(figure_name, data_name, jupyter_notebook):
    average_regret = load_data(figure_name, data_name)
    plot_figure(data_name, average_regret)
    if not jupyter_notebook:
        save_figure(figure_name)


def plot_figure(data_name, line_regret):
    fig = plt.figure() # default (6.4, 4.8) 640x480
    plt.plot(range(1, len(line_regret) + 1), line_regret, label=data_name, color=colors[0])
    plt.xlabel(r'Round $t$')
    plt.ylabel(r'Cumulative Regret $R_t$')
    plt.legend()


def save_figure(figure_name):
    plt.savefig(png_save_path+ '/' + figure_name)
    plt.savefig(eps_save_path + '/' + figure_name + '.eps', format='eps')


def save_data(figure_name, line_name, line_regret):
    data_dict = {line_name: line_regret}
    savemat(mat_save_path + '/' + figure_name + '.mat', data_dict)


def load_data(figure_name, data_name):
    data_dict = loadmat(mat_save_path + '/' + figure_name)
    average_regret = data_dict[data_name][0]
    return average_regret

def plot_supplementary_figure():
    plt.rcParams['figure.subplot.left'] = 0.12
    plt.rcParams['figure.subplot.bottom'] = 0.07
    plt.rcParams['figure.subplot.right'] = 0.96
    plt.rcParams['figure.subplot.top'] = 0.99
    plt.rcParams['font.size'] = 15
    # print(plt.rcParams)
    x = np.arange(0.01, 1, 0.01)
    y = 1 / x ** (1 / 2)
    fig = plt.figure() # default (6.4, 4.8) 640x480
    xcoords = [0.05, 0.2, 0.35]
    for xc in xcoords:
        plt.axvline(x=xc, color='lightgrey')
    ycoords = np.zeros(3)
    for i in range(3):
        ycoords[i] = 1 / xcoords[i] ** (1 / 2)
    for yc in ycoords:
        plt.axhline(y=yc, color='lightgrey')
    plt.xticks((), ())
    plt.yticks((), ())
    # plt.rc('ytick', labelsize=50)
    plt.text(x=xcoords[0], y=0, s=r'$k-1$')
    plt.text(x=xcoords[1], y=0, s=r'$x$')
    plt.text(x=xcoords[2], y=0, s=r'$k$')
    plt.rcParams['font.size'] = 18
    plt.text(x=-0.175, y=ycoords[0], s=r'$\frac{1}{\sqrt{k-1}}$')
    plt.text(x=-0.125, y=ycoords[1] + 0.25, s=r'$\frac{1}{\sqrt{x}}$')
    plt.text(x=-0.125, y=ycoords[2] - 0.25, s=r'$\frac{1}{\sqrt{k}}$')
    plt.text(x=-0.125, y=10, s=r'$\frac{1}{\sqrt{x}}$')
    plt.xlabel(r'$x$', size=15, x=1.015)
    # ax.set_ylabel(r'$\frac{1}{\sqrt{x}}$', size=20, rotation=1, x = -1, y=0.87)
    plt.plot(x, y, color='grey')
    figure_name =  'supplementary_figure'
    save_figure(figure_name)
    plt.show()

# plot_supplementary_figure()
# # modify_figure
# figure_name = 'ucb_convergence_verification'
# line_name = 'UCB'
# modify_regret_figure(figure_name, line_name)