# DFチートシート

## FileIO
```py
#読み込み
## sjisはcp932
## headなし：header=None 設定する場合はname=headerList: []
## 日付変換する場合はparese_date=['date_field'] -> date_field.dt.day.astype('uint8) とかできる
df = pd.read_csv('../../data/test.csv', encoding='utf_8')

# 書き込み
## w:上書 a:追記
df.to_csv(filename, mode='w', write_header=True, index=False, encoding='utf_8')
```

## 基本情報
```py
# 生データ頭5行
df.head()
## ランダム1%のデータ
df_customer.sample(frac=0.01).head(10)

# 列名一覧
'\n'.join(list(df.columns))

# 行数
len(df)

# 行数・列数
df.shape
```

## 統計指標
```py
# 統計情報
df.describe(include='all')

# 平均:mean
## Nullを除外する場合はskipna=True
df.a.mean()

# 最頻値:mode
df.a.apply(lambda x: x.mode())

# 標準分散(var)・標準偏差(std)：引数指定 ddof=0
df.astd(ddof=0)

# パーセンタイル
df.a.quantile(q=np.arange(5)/4)

# パーセンタイルで分類する
df_sum = df.groupby('id').a.sum().reset_index()
df_quantile = df_sum.a.quantile(q=np.arange(5)/4)
df_sum['category'] = df_sum.a.apply(lambda x: 1 if x < df_quantile[0.25] else 2 if x < df_quantile[0.50] else 3 if df_quantile[0.75] else 4)
df_sum.head(10)

# pd.dcutを使う
df_temp = df_receipt.groupby('customer_id')[['amount']].sum()
df_temp['quantile'], bins = pd.qcut(df_receipt.groupby('customer_id')['amount'].sum(), 4, retbins=True)
display(df_temp.head())
print('quantiles:', bins)
```

## 置換・変換
```py
# マッピング置換
# ※inplage=Trueにしないともとのdfに対して上書きされない
df['Sex'].replace(['male','female'], [0,1], inplace=True)
df['Embarked'] = df['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)

# 関数置換
df[target_row] = df.apply(lambda x:replace_fc_sample(x),axis=1)
df[target_row] = df.apply(replace_fc_sample,axis=1)

## 置換用の変数のサンプル
def replace_fc_sample(x):
    if x.open < x.close:
        return 1
    elif x.open > x.close:
        return 2
    else:
        return 0

# ダミー変数化：カテゴリ変数をダミー変数化する場合はone-hot
```

# 型変換・型操作
```py
# Date→文字列
pd.to_datetime(df_customer['birth_day']).dt.strftime('%Y%m%d')
# 文字列→Date
pd.concat([df_customer['customer_id'], pd.to_datetime(df_customer['application_date'])], axis=1) 

# 数値→文字列
df_receipt['sales_ymd'].astype('str')
# unix秒→Date
pd.to_datetime(df_receipt['sales_epoch'], unit='s')

# Date 年/月/日 year/month/day
df['sale_datetime'].dt.year
## mmのように0埋め2桁の場合はstrftime
df['sale_datetime'].dt.strftime('%m')
## 経過月数のような年月計算はrelativedelta
df_tmp['elapsed_date'] = df_tmp[['sales_ymd', 'application_date']].apply(lambda x: 
                                    relativedelta(x[0], x[1]).years * 12 + relativedelta(x[0], x[1]).months, axis=1)

# str 前3文字
df['name'].str[0:3]

```

## 表示・クエリ
```py
# 列名指定
df_receipt[['sales_ymd','customer_id','product_cd','amount']]

# 条件指定
df_receipt.query('customer_id=="CS018205000001"')
## 文字列メソッド contains endswith startswith match
df_receipt.query('customer_id.str.startswith("a")', engine='python')
df_customer.query('status_cd.str.contains("[1-9]$", regex=True)',engine='python').head(10)

# ソート
df.sort_values('col_name', ascending=False)
## 複数列ソートは配列を渡す sort_values([a,b])
## 加工後にソートするならreset_indexする
df_receipt.groupby('store_cd').agg({'amount':'mean'}).reset_index().sort_values('amount',ascending=False).head(5)
```

## 集計（カテゴリ値）
```py
# ユニーク値
df['a'].unique()

# ユニーク件数
df['a'].nunique()

# ユニーク値ごとに集計
x=df.a.value_counts()
x=df.group_by('a').size()
```

## 集計（数値）
```py
# 1列集計：関数
df_receipt.groupby('customer_id').sales_ymd.max().reset_index().head(10)
## 複数キー集計はgroupbyに配列を渡す

# 複数列集計：agg sum/count/max/min/mean(平均)/median(中央)/std(標準偏差)/nunique(ユニークカウント)
df_receipt.groupby('store_cd').agg({'amount':'sum', 'quantity':'sum'}).reset_index()
df_groupby('key').a.agg([min,max])

## 1列複数関数
df_tmp = df_receipt.groupby('customer_id').agg({'sales_ymd':['max','min']}).reset_index().head(10)
df_tmp.columns = ["_".join(pair) for pair in df_tmp.columns] #複数関数の場合、列名はpairになっている
df_tmp.query('sales_ymd_max != sales_ymd_min').head(10)

# Groupで圧縮しない（各行に合計値をセット）：transform
df_train['target_mean'] = df_train.groupby('keyword')['target'].transform('mean')

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
## ピボットテーブルを展開する場合はstack
## 行名がlevel_1とか0になるので修正する
pivot_df2 = pivot_df2.set_index('age_rank').stack().reset_index().rename(columns={'level_1':'gender_cd', 0: 'amount'})
```

## 集計関数
```py
# ランク
df_tmp = pd.concat([df_receipt[["customer_id","amount"]], df_receipt["amount"].rank(ascending=False, method='first')], axis=1)
df_tmp.columns = ['customer_id','amount','rank']
df_tmp.sort_values('rank', ascending=False).head(10)
```

## 行単位の計算
```py
# 前行からの差分を取る
df.diff()

# 前行までの値を使って計算
df.expanding().mean()
```

## df操作
```py
# 列名変更
df.rename(columns={'A': 'a'})

# 列削除
X_train = train.drop('Survived', axis = 1)

# dfくっつける
pd.concat([df1,df2], axis=1)

# df結合 left/right/inner/outer
application_train = pd.merge(application_train, previous_loan_counts, on='SK_ID_CURR', how='left')
## 重複列を削除する場合はdrop_duplicates
## indexで結合する場合は leftDf.join(rightDf)

# コピー
df_tmp = df_product.copy()

```
