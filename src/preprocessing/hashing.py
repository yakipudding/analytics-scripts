# 機械学習のための特徴量エンジニアリングより
# ハッシング

import pandas as pd
import json

# 最初の10,000件のレビューを読み込み
with open('data/yelp/yelp_academic_dataset_review.json') as f:
    js = []
    for i in range(10000):
        js.append(json.loads(f.readline()))

review_df = pd.DataFrame(js)
# mにbusiness_idのユニーク数を代入
m = len(review_df['business_id'].unique())

m

from sklearn.feature_extraction import FeatureHasher

# ハッシュ化
h = FeatureHasher(n_features=m, input_type='string')
f = h.transform(review_df['business_id'])

# 変換後の特徴量が解釈が困難であることを確認
review_df['business_id'].unique().tolist()[0:5]

f.toarray()

# 変換後の特徴量のストレージサイズが大きく減っていることを確認
from sys import getsizeof
print('Our pandas Series, in bytes: ', getsizeof(review_df['business_id']))
print('Our hashed numpy array, in bytes: ', getsizeof(f))