"""
原创
绘制给定相关系数的代码
原理：线性代数的线性变换，奇异值分解
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_cov2(rho, under, upper, num):
    x = np.random.uniform(under, upper, num)
    y = np.random.uniform(under, upper, num)
    x_to_one = (x-np.mean(x)) / np.sqrt(np.var(x))
    y_to_one = (y-np.mean(y)) / np.sqrt(np.var(y))
    plt.scatter(x_to_one, y_to_one)
    plt.hlines(0, -5, 5, colors='red', linestyles='--')
    plt.vlines(0, -5, 5, colors='red', linestyles='--')
    plt.title("before_tran")
    plt.show()
    cov_matrix = np.array([[1, rho],
                           [rho, 1]])
    U, S_diag, V_T = np.linalg.svd(cov_matrix)
    S = np.diag(S_diag)
    S_tran = np.sqrt(S)
    data = np.random.normal(0, 1, size=(2, num))
    tranformed_data = U @ S_tran @ data
    plt.scatter(tranformed_data[0, :], tranformed_data[1, :])
    direct1 = [4, U[0, 0]*5]
    direct2 = [4, U[0, 1]*5]
    plt.text(U[0, 0]*5, U[0, 1]*5, f"Correlation coefficient={rho}")
    plt.plot(direct1, direct2, linestyle='--', color='red', linewidth=3)
    plt.title("after_tran")
    plt.show()


def main():
    rho = 0.8
    num = 200
    plot_cov2(rho, -5, 5, num)


if __name__ == '__main__':
    main()

