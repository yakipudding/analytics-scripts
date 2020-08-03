# 棒グラフ
import seaborn as sns
import pandas as pd

data = pd.read_csv('../../data/OnlineNewsPopularity.csv', delimiter=', ', engine='python')
## x：横軸（比較する数値）
## hue：グラフを重ねる条件（分類）
sns.countplot(x='FamilySize', data=data, hue='Survived')