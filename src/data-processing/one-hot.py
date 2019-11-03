# 機械学習のための特徴量エンジニアリングより
# one-hotエンコーディング/ダミーコーディング

import pandas as pd
from sklearn import linear_model

# 3つの都市におけるアパートの家賃のデータセットを設定
df = pd.DataFrame({
    'City': ['SF', 'SF', 'SF', 'NYC', 'NYC', 'NYC', 'Seattle', 'Seattle', 'Seattle'],
    'Rent': [3999, 4000, 4001, 3499, 3500, 3501, 2499, 2500, 2501]
})

df['Rent'].mean()

# One-Hotエンコーディングをカテゴリ値であるcity列に適用
# 特徴量をOne-Hotエンコーディングで生成した列に、ターゲット変数を家賃に指定し、線形回帰モデルを学習
one_hot_df = pd.get_dummies(df, prefix=['city'])
one_hot_df

model = linear_model.LinearRegression()
model.fit(one_hot_df[['city_NYC', 'city_SF', 'city_Seattle']], one_hot_df['Rent'])
model.coef_

model.intercept_

# ダミーコーディングを利用して線形回帰モデルを学習
dummy_df = pd.get_dummies(df, prefix=['city'], drop_first=True)
dummy_df

model.fit(dummy_df[['city_SF', 'city_Seattle']], dummy_df['Rent'])
model.coef_

model.intercept_

# Effectコーディング
effect_df = dummy_df.copy()
effect_df.loc[3:5, ['city_SF', 'city_Seattle']] = -1.0
effect_df

model.fit(effect_df[['city_SF', 'city_Seattle']], effect_df['Rent'])
model.coef_

model.intercept_
