# 機械学習のための特徴量エンジニアリングより
## k-meansクラスタリングで次元削減

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import manifold, datasets

# スイスロール上にランダムにデータを生成する
X, color = datasets.samples_generator.make_swiss_roll(n_samples=1500)

# k-meansでそのデータを100個のクラスタで近似する
clusters_swiss_roll = KMeans(n_clusters=100, random_state=1).fit_predict(X)

# 所属するk-meansのクラスタIDごとに色分けをしてデータをプロットする
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=clusters_swiss_roll, cmap='Spectral')

plt.show()