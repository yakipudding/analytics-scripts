# 欠損値補完
```py
# 列ごとのnullカラム数
df.isnull().sum()
## 欠損値が多い場合、列ごと削除したほうが良い
## 欠損値が少ない場合、平均値補完したほうが良い
```

## fillna
```py
df['Sex'].fillna('male', inplace=True)
# np.mean(df['amount'])で補完したり
```

## sklearn.impute.SimpleImputer
```py
from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
# storategy: mean(default) / median / most_frequent / constant: fill_value(default=None)をセット

# fit_transform: trainのデータでfit(mean計算) + transform
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
# validはtrainで計算したmeanを使用してtransformする
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Imputation removed column names
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns
```

他には欠損値補完とエンコーディングをまとめられる[Pipeline](../learning/pipeline.md)がある