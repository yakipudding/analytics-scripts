import pandas as pd
import json

encoding_utf8 = 'utf_8'
encoding_sjis = 'cp932'

write_mode_write = 'w' #上書き
write_mode_add = 'a' #追記

def read_csv_to_df(filename, has_header=True, header_list=[], sep=',', encoding=encoding_utf8):
  df = pd.DataFrame()
  if has_header:
    df = pd.read_csv(filename, sep=sep, encoding=encoding)
  else:
    df = pd.read_csv(filename, header=None, name=header_list, sep=sep, encoding=encoding)
  
  return df

def write_df_to_csv(df, filename, write_header=True, sep=',', mode=write_mode_write, encoding=encoding_utf8):
  df.to_csv(filename, mode=mode, header=write_header, sep=sep, index=False, encoding=encoding)

def read_json_to_df(filename):
  df = pd.DataFrame()
  with open(filename) as biz_file:
      df = pd.DataFrame([json.loads(x) for x in biz_file.readlines()])
  
  return df