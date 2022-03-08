import os
import numpy as np
import math
import matplotlib
matplotlib.rcParams['backend'] = "TKAgg"

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import imageio 
import set_data
'''
data = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0]]
'''
def take_log(n, data):
    tmp = []
    for i in range(n):
        tmp.append([])
        for j in range(n):
            tmp[i].append(0)
    
    for i in range(n):
        for j in range(n):
            tmp[i][j] = math.log(data[i][j]+0.0000000000000000000000000000001, 10)

    return tmp

def plot_examples(colormaps, data, i, size):

    n = len(colormaps)
    fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3), constrained_layout=True, squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-3, vmax = 30)
        fig.colorbar(psm, ax=ax)

    plt.savefig( str(i) + ".png")

filenames = []
size = 100000000000000000000000000000
now_slime_state = []
now_weight = []
initial_food = []
n = 100
for i in range(n):
    now_slime_state.append([])
    now_weight.append([])
    initial_food.append([])
    for j in range(n):
        now_slime_state[i].append(0)
        now_weight[i].append([])
        now_weight[i][j].append(0)
        now_weight[i][j].append(0)
        now_weight[i][j].append(0)
        now_weight[i][j].append(0)
        initial_food[i].append(0)


#initial_food[70][50] = 100
#initial_food[80][70] = 100
#initial_food[30][40] = 100
now_slime_state[0][0] = size

ans = [now_slime_state, now_weight]
for i in range(1000):
    ans = set_data.output(n, initial_food, ans[0], ans[1])
    '''
    if (i == 199):
        hot = cm.get_cmap('hot', 256)
        plot_examples([hot], ans[0], i, size)
        filenames.append(str(i)+'.png')
'''
    hot = cm.get_cmap('hot', 256)

    data = take_log(n, ans[0])

    plot_examples([hot], data, i, size)
    filenames.append(str(i)+'.png')


with imageio.get_writer('mygif_1000_25_30.gif', mode = 'I') as writer:

    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

for filename in set(filenames):
    os.remove(filename)
