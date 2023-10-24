import numpy as np
from sympy import *

# 反函数inverse function
x, y = symbols('x y')


def inv_func(func, x):
    '''
    计算反函数
    :param func: 原函数
    :param x: 自变量
    :return:
    '''
    return solve(func, x)[0]


def func_density(fx, func, x, y):
    '''
    已知原分布概率密度求函数的概率密度
    :param fx: 自变量的分布
    :param func: 原函数
    :param x: 原分布的自变量
    :param y: 因变量，新分布的自变量
    :return:
    '''
    x1 = solve(func, x)[0]
    fy = fx.subs({x: x1}) * Abs(diff(x1, y))  # 导数的绝对值
    return fy


def combine(n, m):
    '''
    计算组合数
    :param n:
    :param m:
    :return:
    '''
    return factorial(n) / (factorial(m) * factorial(n - m))


def gen_sym_matrix(n, type='randn', low=0, high=10, seed=None):
    '''
    生成实对称矩阵
    :param n: 生成对称矩阵的维度
    :param type: 生成随机数类型，默认标准正态分布
    :param low: 整数随机数上限，默认包含0
    :param high: 整数随机数上限，默认不包含10
    :param seed: 随机数种子，默认为None
    :return:
    '''
    np.random.seed(seed)
    if type == 'randint':
        X = np.random.randint(low, high, size=(n, n))
    elif type == 'rand':
        X = np.random.rand(n, n)
    else:
        X = np.random.randn(n, n)
    X = np.triu(X)  # 上三角矩阵
    X += X.T - np.diag(X.diagonal())
    return X


if __name__ == '__main__':
    np.random.seed(None)
    a = gen_sym_matrix(10, 'randint')
    print(a)
    print(0)

