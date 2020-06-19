# 機械学習のための特徴量エンジニアリングより
# スケーリング
import pandas as pd
import numpy as np
import sklearn.preprocessing as preproc

# Online News Popularity データセットの読み込み
df = pd.read_csv('../../data/OnlineNewsPopularity.csv', delimiter=', ', engine='python')

# 元データ（記事中の単語数）
df['n_tokens_content'].values

# Min-Max スケーリング：最小値0,最大値1の正規化
df['minmax'] = preproc.minmax_scale(df[['n_tokens_content']])
df['minmax'].values

# 標準化：平均0,分散1
df['standardized'] = preproc.StandardScaler().fit_transform(df[['n_tokens_content']])
df['standardized'].values

# 標準化：平均0,標準偏差1
## skleanのpreprocessing.scaleを利用するため、標本標準偏差で計算されている
df_sales_amount = df.groupby('customer_id').agg({'amount':'sum'}).reset_index()
df_sales_amount['amount_ss'] = preproc.scale(df_sales_amount['amount'])
df_sales_amount.head(10)

# L2 正規化
df['l2_normalized'] = preproc.normalize(df[['n_tokens_content']], axis=0)
df['l2_normalized'].values

# Loge
df_sales_amount['amount_loge'] = np.log(df_sales_amount['amount'] + 1)