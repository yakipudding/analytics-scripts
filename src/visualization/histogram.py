# 機械学習のための特徴量エンジニアリングより
# ヒストグラム
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../../data/OnlineNewsPopularity.csv', delimiter=', ', engine='python')

# 1. レビュー件数のヒストグラムを描画
sns.set_style('whitegrid')
fig, ax = plt.subplots()
df['n_tokens_content'].hist(ax=ax, bins=100)
ax.set_yscale('log')
ax.tick_params(labelsize=14)
ax.set_xlabel('Review Count', fontsize=14)
ax.set_ylabel('Occurrence', fontsize=14)

plt.show()

# 2. ヒストグラムに十分位数を上書きする

# 十分位数の計算
deciles = df['n_tokens_content'].quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9])

sns.set_style('whitegrid')
fig, ax = plt.subplots()
df['n_tokens_content'].hist(ax=ax, bins=100)
for pos in deciles:
    handle = plt.axvline(pos, color='r')
ax.legend([handle], ['deciles'], fontsize=14)
ax.set_yscale('log')
ax.set_xscale('log')
ax.tick_params(labelsize=14)
ax.set_xlabel('Review Count', fontsize=14)
ax.set_ylabel('Occurrence', fontsize=14)

plt.show()

# 3. 対数変換の前後でレビュー件数のヒストグラムを比較する
import numpy as np

# 例2-2で読み込んだ Yelp データセットの
# データフレーム df を使用して、レビュー件数を対数変換する。
# レビュー件数 0 を対数変換してマイナス無限大になるのを防ぐために
# 対数変換の前に生データに 1 を加算していることに注意。
df['log_n_tokens_content'] = np.log10(df['n_tokens_content'] + 1)

fig, (ax1, ax2) = plt.subplots(2,1)
df['n_tokens_content'].hist(ax=ax1, bins=100)
ax1.tick_params(labelsize=14)
ax1.set_xlabel('review_count', fontsize=14)
ax1.set_ylabel('Occurrence', fontsize=14)

df['log_n_tokens_content'].hist(ax=ax2, bins=100)
ax2.tick_params(labelsize=14)
ax2.set_xlabel('log10(review_count))', fontsize=14)
ax2.set_ylabel('Occurrence', fontsize=14)

plt.show()

# 4. ヒストグラムに全体の分布を推定した折れ線グラフを表示する場合、sns.distplotを用いる(kde=Falseで消える)
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
word=tweet[tweet['target']==1]['text'].str.split().apply(lambda x : [len(i) for i in x])
sns.distplot(word.map(lambda x: np.mean(x)),ax=ax1,color='red')
ax1.set_title('disaster')
word=tweet[tweet['target']==0]['text'].str.split().apply(lambda x : [len(i) for i in x])
sns.distplot(word.map(lambda x: np.mean(x)),ax=ax2,color='green')
ax2.set_title('Not disaster')
fig.suptitle('Average word length in each tweet')
