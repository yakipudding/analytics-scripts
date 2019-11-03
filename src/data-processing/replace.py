import pandas as pd

# 関数で置換
def replace_df_by_fc(df, target_row, replace_fc = replace_fc_sample()):
  df[target_row] = df.apply(lambda x:replace_fc_sample(x),axis=1)

# 置換用の変数のサンプル
def replace_fc_sample(x):
    if x.open < x.close:
        return 1
    elif x.open > x.close:
        return 2
    else:
        return 0
