# ヒストグラム
```py
plt.hist(df['a'], range(0, 10000),bins=50)

ax.hist(tweet_len,color='red')

# dfで頻度を集計する場合
## bins:基数
df['n_tokens_content'].hist(ax=ax, bins=100)

# ヒストグラム
## kde: 全体の分布を推定した折れ線グラフを表示するかどうか
sns.distplot(a=df[a], kbe=True)

# 近似曲線のみ
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)

# 2Dの近似曲線
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")
```

## 十分位数を上書きする
```py
# 十分位数の計算
deciles = df['n_tokens_content'].quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9])

fig, ax = plt.subplots()
df['n_tokens_content'].hist(ax=ax, bins=100)
for pos in deciles:
    handle = plt.axvline(pos, color='r')
ax.legend([handle], ['deciles'], fontsize=14)

plt.show()
```
