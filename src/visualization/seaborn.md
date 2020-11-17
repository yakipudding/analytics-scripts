# Seaborn

## imports
```py
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
```
pd.plotting.register_matplotlib_converters()：pandas型変換
%matplotlib inline：Notebookでインラインに画像表示

## 定義
```py
# figとaxを一気に作る
fig, ax = plt.subplots()
ax.plot(x,y)

# 複数グラフ
fig = plt.figure()
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
ax.plot(x, y)
```

## データ操作
```py
# index指定してcsv読込
df = pd.read_csv(filepath, index_col=index_col_name)

# 対数変換
df['log_n_tokens_content'] = np.log10(df['n_tokens_content'] + 1)

# target列(カテゴリ値)を値ごとに集計
x=tweet.target.value_counts()
```

## レイアウト
```py
# グラフ縦横比率
plt.figure(figsize=(16,6))

# タイトル
ax.set_title('disaster tweets')
fig.suptitle('Characters in tweets')

# ラベル
ax.set_ylabel('Occurrence', fontsize=14)

# スケール
ax.set_yscale('log')

# スタイル
sns.set_style('whitegrid')

# 目盛スタイル
ax.tick_params(labelsize=14)

# 凡例を表示する
fig.legend(loc='upper right', bbox_to_anchor=(1,1), bbox_transform=ax.transAxes, title='凡例タイトル')
```

## タプルの配列からソートしてxy軸作成
```py
# TOP10を描画
top=sorted(dic.items(), key=lambda x:x[1],reverse=True)[:10] 
#  top:[('the', 1524),('a', 1115), ...] タプルの配列
# *top:('the', 1524) ('a', 1115)... ※要素がアンパックされる
x,y=zip(*top) # zip:複数リストの要素を取得
# x:('the','a',...) y:(1524,1115,...)
plt.bar(x,y)
```

## dictionaryからxy軸作成
```py
plt.plot(list(results.keys()), list(results.values()))
```

## ヒートマップ
```py
sns.heatmap(data=flight_data, annot=True)
```