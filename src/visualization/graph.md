# グラフ

```py
# 縦棒グラフ
sns.barplot(x,y)

# 集計して棒グラフ
## x：横軸（比較する数値）
## hue：グラフを重ねる条件（分類）
sns.countplot(x='FamilySize', data=data, hue='Survived')

# 横棒グラフ
sns.barplot(x=y,y=x)

# 折れ線グラフ
## dfのindexが横軸、列名がラベルになる。列ごとに重ねる
sns.lineplot(data=df)

# 散布図
## hue：グラフの色を変更する条件（分類）
sns.scatterplot(x=df['x'], y=df['y'], hue=df[hue])
ax.scatter(x=df['x'], y=df['y'])

# 散布図（＋回帰直線）
sns.regplot(x=df['x'], y=df['y'])

# 散布図（＋回帰直線が複数）　hueあり
sns.lmplot(x="x", y="y", hue="smoker", data=df)
```

