# 棒グラフ
import seaborn as sns
import pandas as pd

data = pd.read_csv('../../data/OnlineNewsPopularity.csv', delimiter=', ', engine='python')

## dfから集計して棒グラフ表示
### x：横軸（比較する数値）
### hue：グラフを重ねる条件（分類）
sns.countplot(x='FamilySize', data=data, hue='Survived')

## 事前に集計して棒グラフ表示
import matplotlib.pyplot as plt
x=tweet.target.value_counts() # targetを値ごとに集計
sns.barplot(x.index,x)
plt.gca().set_ylabel('samples') # y軸ラベル

## 横棒グラフ
sns.barplot(x=y,y=x)