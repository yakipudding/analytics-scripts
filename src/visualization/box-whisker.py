# 機械学習のための特徴量エンジニアリングより
# 箱ひげ図

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../../data/OnlineNewsPopularity.csv', delimiter=', ', engine='python')

# 分類器のパフォーマンスを可視化して比較する
search_results = pd.DataFrame.from_dict({
    'aaa': df['n_tokens_content'],
    'bbb': df['n_tokens_content'],
})

# matplotlibでグラフを描く。ここでSeabornはグラフの見た目を整える為に用いている。
sns.set_style("whitegrid")
ax = sns.boxplot(data=search_results, width=0.4)
ax.set_ylabel('Accuracy', size=14)
ax.tick_params(labelsize=14)

plt.show()