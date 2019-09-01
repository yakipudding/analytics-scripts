import pandas as pd

def read_csv_to_df(filename, has_header=True, header_list=[], sep=',', encoding='utf_8'):
  #shift_jisの場合はencoding=cp932
  df = pd.DataFrame()
  if has_header:
    df = pd.read_csv(filename, sep=sep, encoding=encoding)
  else:
    df = pd.read_csv(filename, header=None, name=header_list, sep=sep, encoding=encoding)
  
  return df

def write_df_to_csv(df, filename, write_header=True, sep=',', mode='w', encoding='utf_8'):
  #shift_jisの場合はencoding=cp932
  #mode w:上書 a:追記
  df.to_csv(filename, mode=mode, header=write_header, sep=sep, index=False, encoding=encoding)
