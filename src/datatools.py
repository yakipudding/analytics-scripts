import pandas as pd
import fileiotools as fileio

def replace_df_by_list(df, from_list=[], to_list=[]):
  #from_list: 変換前
  #to_list: 変換前
  #※列指定できないので注意
  return df.replace(from_list, to_list)

df = fileio.read_csv_to_df('../data/test.csv')
df2 = replace_df_by_list(df,['田中 太郎','山田 花子'],['田中 二太郎','山田 華子'])
print(df2)
