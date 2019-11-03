import pandas as pd

# csv読み込み
df = pd.read_csv('../../data/test.csv', encoding='utf_8')

# 生データ
print('■生データ')
print(df)

# 列名一覧
print('\n■列名')
print('\n'.join(list(df.columns)))

# 統計情報
print('\n■統計情報')
print(df.describe(include='all'))

# 列加工 ###########################################

# 置換用変数
def replace_fc(x):
    return str(int(x.age/10)) + '0年代'

# 列置換
print('■列置換 age→年代')
df['age_range'] = df.apply(lambda x:replace_fc(x),axis=1)

# 列集計
grouping_row = 'age_range'
print('\n■' + grouping_row + '列集計')
df_count = df[grouping_row].value_counts()
df_count_p = df[grouping_row].value_counts(normalize=True)
print(pd.concat([df_count, df_count_p], axis=1))

# ピボット（クロス集計）
grouping_rows_index = ['sex'] ##集計：列
grouping_rows_columns = ['学年'] #集計：行
pivot_values = 'id' #値
pivot_value_fc = 'count' #値関数：sum/count/max/min/mean
view_sum = True #集計業を表示するか
print('\n■' + ','.join(grouping_rows_index) + '/' + ','.join(grouping_rows_columns) + ' ピボット集計')
pivot_df = pd.pivot_table(df, index=grouping_rows_index, columns=grouping_rows_columns, values=pivot_values, aggfunc=pivot_value_fc, margins=view_sum)
print(pivot_df)