# 機械学習のための特徴量エンジニアリングより
# スケーリング
import pandas as pd
import sklearn.preprocessing as preproc

# Online News Popularity データセットの読み込み
df = pd.read_csv('../../data/OnlineNewsPopularity.csv', delimiter=', ', engine='python')

# 元データ（記事中の単語数）
df['n_tokens_content'].values

# Min-Max スケーリング
df['minmax'] = preproc.minmax_scale(df[['n_tokens_content']])
df['minmax'].values

# 標準化（定義より出力が負になることもある）
df['standardized'] = preproc.StandardScaler().fit_transform(df[['n_tokens_content']])
df['standardized'].values

# L2 正規化
df['l2_normalized'] = preproc.normalize(df[['n_tokens_content']], axis=0)
df['l2_normalized'].values