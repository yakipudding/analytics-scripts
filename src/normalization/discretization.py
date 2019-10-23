# 機械学習のための特徴量エンジニアリングより
# 離散化

## 固定幅の離散化
import numpy as np
np.random.seed(seed=1)

### 1. 固定値幅
# 除算により 0-9 までの階級を割り当てる
# 0から99までの一様分布整数に対して
small_counts = np.random.randint(0, 100, 20)
np.floor_divide(small_counts, 10)

### 2. 指数幅の階級
# 対数変換により指数幅の階級を割り当てる
# 複数の桁にまたがるカウントデータの配列に対して
large_counts = [296, 8286, 64011, 80, 3, 725, 867, 2215, 7689, 11495, 91897, 
                44, 28, 7971, 926, 122, 22222]
np.floor(np.log10(large_counts))

## 分位数による離散化
import pandas as pd

# 四分位数に変換
pd.qcut(large_counts, 4, labels=False)
# 分位数の計算
large_counts_series = pd.Series(large_counts)
large_counts_series.quantile([0.25, 0.5, 0.75])