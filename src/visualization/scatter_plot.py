# 機械学習のための特徴量エンジニアリングより
# 散布図
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/OnlineNewsPopularity.csv', delimiter=', ', engine='python')

# ニュース記事内に含まれる単語数 'n_tokens_content' に対数変換を施す
df['log_n_tokens_content'] = np.log10(df['n_tokens_content'] + 1)

# 散布図
fig2, (ax1, ax2) = plt.subplots(2,1)
ax1.scatter(df['n_tokens_content'], df['shares'])
ax1.tick_params(labelsize=14)
ax1.set_xlabel('Number of Words in Article', fontsize=14)
ax1.set_ylabel('Number of Shares', fontsize=14)

ax2.scatter(df['log_n_tokens_content'], df['shares'])
ax2.tick_params(labelsize=14)
ax2.set_xlabel('Log of the Number of Words in Article', fontsize=14)
ax2.set_ylabel('Number of Shares', fontsize=14)

plt.show()