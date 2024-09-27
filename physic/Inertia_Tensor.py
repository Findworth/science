"""
给孩子个star吧

固连在刚体上的随意选择的轴可以通过对惯量张量进行线性变换来消去惯量积
1. 求惯量矩阵的特征值
2. 新的惯量张量对角线上的元素为主转动惯量，也就是特征值
3. 变化后，惯量主轴的方向"摆正"了，方向就是新的惯量矩阵的特征向量方向
"""
__author__ = "小耿物理"

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False

S = np.array([[5, 4],
              [4, 5]])
# 求S的特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(S)
print(f"这是特征值：{eigenvalues}")
print(f"单位特征向量:{eigenvectors}")
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)
Z = 5 * X ** 2 + 5 * Y ** 2 + 8 * X * Y
# 斜椭圆的轴沿着特征向量的指向
origin = np.array([[0],
                   [0]])
fig, axs = plt.subplots(1, 2, figsize=(16, 10))
axs[0].contour(X, Y, Z, levels=[1])
axs[0].scatter(0, 0, color="black")
axs[0].plot([0, eigenvectors[:][0][0]], [0, eigenvectors[:][0][1]], linestyle="--", color="red")
axs[0].plot([0, eigenvectors[:][1][0]], [0, eigenvectors[:][1][1]], linestyle="--", color="red")
axs[0].plot([0, 0], [-1, 1], linestyle="--", color="black")
axs[0].plot([-1, 1], [0, 0], linestyle="--", color="black")
axs[0].set_title("未进行主轴变换")
# 为消去惯量积，进行对称矩阵的对角化, 此时X相当于进行了变量代换 X = X @ 特征向量矩阵
diag_S = np.diag(eigenvalues)
Z = 9 * X ** 2 + Y ** 2
axs[1].contour(X, Y, Z, levels=[1])
axs[1].plot([0, 0], [-1, 1], linestyle="--", color="black")
axs[1].plot([-1, 1], [0, 0], linestyle="--", color="black")
axs[1].set_title("主轴变换后")
plt.show()
