# -*- coding: utf-8 -*-
# ----------------------------------------------------
# Copyright (c) 2017, Wray Zheng. All Rights Reserved.
# Distributed under the BSD License.
# ----------------------------------------------------

from matplotlib import pyplot
from gmm import *

# 载入数据
Y = np.loadtxt("gmm.data")
matY = np.matrix(Y, copy=True)
print(Y.shape)
pyplot.plot(Y[:, 0], Y[:, 1],'ko', label="class1")
pyplot.show()

# 模型个数，即聚类的类别个数
K = 2

# 计算 GMM 模型参数
mu, cov, alpha = gmm_em(matY, K, 100)

# 根据 GMM 模型，对样本数据进行聚类，一个模型对应一个类别
N = Y.shape[0]
# 求当前模型参数下，各模型对样本的响应度矩阵
gamma = e_step(matY, mu, cov, alpha)
# 对每个样本，求响应度最大的模型下标，作为其类别标识
category = gamma.argmax(axis=1).flatten().tolist()[0]
# 将每个样本放入对应类别的列表中
class1 = np.array([Y[i] for i in range(N) if category[i] == 0])
class2 = np.array([Y[i] for i in range(N) if category[i] == 1])
print("____________")
print(class1.shape)
print(class2.shape)
# 绘制聚类结果
pyplot.plot(class1[:, 0], class1[:, 1], 'rs', label="class1")
pyplot.plot(class2[:, 0], class2[:, 1], 'bo', label="class2")
pyplot.legend(loc="best")
pyplot.title("GMM Clustering By EM Algorithm")
pyplot.show()