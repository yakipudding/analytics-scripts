# チートシート

## csv読み込み
```py
df = pd.read_csv('../../data/test.csv', encoding='utf_8')
```

## 生データ
```py
# 生データ頭5行
df.head()

# 列名一覧
'\n'.join(list(df.columns))

# 列数
len(df)

# 列ごとのnullカラム数
df.isnull().sum()

# 統計情報
df.describe(include='all')
```

## 欠損値補完
```py
df.['Sex'].fillna(('male'), inplace=True)
# 平均値補完
data['Fare'].fillna(np.mean(data['Fare']), inplace=True)
```

## 置換
```py
# マッピング置換
# ※inplage=Trueにしないともとのdfに対して上書きされない
df['Sex'].replace(['male','female'], [0,1], inplace=True)
df['Embarked'] = df['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)

# 関数置換
df[target_row] = df.apply(lambda x:replace_fc_sample(x),axis=1)

## 置換用の変数のサンプル
def replace_fc_sample(x):
    if x.open < x.close:
        return 1
    elif x.open > x.close:
        return 2
    else:
        return 0
```

## 集計
```py
# 列集計
## 集計キー列
grouping_row = 'SK_ID_CURR'
## 集計値列
summary_row = 'SK_ID_BUREAU'
summary_row_name = 'previous_loan_counts'
previous_loan_counts = bureau.groupby(grouping_row, as_index=False)[summary_row].count().rename(columns={summary_row: summary_row_name})

# ピボット（クロス集計）
## 集計：列
grouping_rows_index = ['sex']
## 集計：行
grouping_rows_columns = ['学年']
## 集計：値
pivot_values = 'id' 
## 値関数：sum/count/max/min/mean
pivot_value_fc = 'count' 
## 集計行を表示するか
view_sum = True
pivot_df = pd.pivot_table(df, index=grouping_rows_index, columns=grouping_rows_columns, values=pivot_values, aggfunc=pivot_value_fc, margins=view_sum)
```

## df操作
```py
# 列削除
X_train = train.drop('Survived', axis = 1)

# df結合
application_train = pd.merge(application_train, previous_loan_counts, on='SK_ID_CURR', how='left')
```