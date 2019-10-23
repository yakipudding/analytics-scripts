# 機械学習のための特徴量エンジニアリングより
# PCA(主成分分析)

from sklearn import datasets
from sklearn.decomposition import PCA

# データの読み込み
digits_data = datasets.load_digits()
n = len(digits_data.images)

# それぞれの画像は8 × 8の配列としてあらわされている。
# この配列をPCAへの入力とするために1次元へと倒す。
image_data = digits_data.images.reshape((n, -1))
image_data.shape

# 各画像の数値の正解ラベルを取得
labels = digits_data.target
labels

# データセットに対してPCAを適用する
# 主成分の数は、少なくとも全体の分散の80%が説明できる水準となるよう自動的に選ばれる
pca_transformer = PCA(n_components=0.8)
pca_images = pca_transformer.fit_transform(image_data)
pca_transformer.explained_variance_ratio_

pca_transformer.explained_variance_ratio_[:3].sum()

# 結果を可視化する
# %matplotlib inline
# %matplotlib notebook
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(100):
    ax.scatter(pca_images[i,0], pca_images[i,1], pca_images[i,2],
    marker=r'${}$'.format(labels[i]), s=64)

ax.set_xlabel('Principal component 1')
ax.set_ylabel('Principal component 2')
ax.set_zlabel('Principal component 3')