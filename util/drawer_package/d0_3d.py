# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot([0,1],[1, 2],[3, 4], label='a', linestyle='-', linewidth=2, color='0', marker='H')


    ax.legend()  # 显示图例
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    plt.xlim(0, 2)
    plt.ylim(0, 2)

    ax.view_init(elev=20, azim=20)  # 调整视角

    plt.show()