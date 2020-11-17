# Python
## 演算
- 除算
  - 2.X系：整数同士の除算はintになる
  - 3.X系：整数同士の除算はfloat（浮動小数点）になる
- 累乗：`**`
- 商：`//`
  - 小数点以下切り捨て
- boolの演算：0/1になる
  - `true + false + false == 1`とかに使える

## 文字列
- f文字列（テンプレート構文てきな）
  - `f"{a} is {b}"`
- r：/\が入るとき（生文字）
  - `r"c://..."`

## list
- 定義：`a = [1, 2, 3, 4, 5]`
- 要素に後ろからアクセス：`a[-i]`
- 部分リストにアクセス(スライシング)
  - `a[0:2]` [1,2] #インデックス0-(2-1)の要素まで
  - `a[:-1]` [1,2] #インデックス0-最後から1個手前の要素まで
- 要素数：`len(list)`
- 追加：`list.append(item)`
- 存在するかどうか：`item in list	`
- index：`list.index(item)`
- map：`[item式 for item in list]`
- 合計：`sum(list)`
  - True/FalseのリストだとTrueの数

## dictionary
- キーバリューペア
- 定義：`dic = {'a' :1}`
- 値を確認：`dic['a'] #1`
- 新しい要素を追加：`dic['b'] = 2`
- 要素の存在確認：`'a' in dic`
- キーバリューのlist：`dic.items() #key:item[0], value:item[1]`

## forのTips
- listのindexも取得したいとき
	- `for doc, index in enumerate(doc_list):`
	- それかrangeつかう

## range
- startからend-1までの整数からなるリストを作成する
  - `range(0,10) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- startからend-1までのstepで指定された値だけ増加するリストを作成する
  - `range(0,10,3) #[0, 3, 6 ,9]`

## class
- 定義：`class クラス名:`
- コンストラクタ：`def __init__(self, 引数, ...)`

## setオブジェクト
- list要素の重複削除に用いられる事が多い
- 集合演算が使えるオブジェクト
  - set([1,2,3]) - set([1,2]) = set([3])
- 定義：`set(list)`

## Counterオブジェクト
- `from collections import Counter`
- ユニークな要素を数える
- 定義：`Counter(list)`
  - 中身はdictionary
- 最頻値：`counter.most_common(1)`

## インポート元のパスを増やす
- `sys.path.append(絶対パス)`

## lambda
- 関数の定義を省略化
- 定義：`lambda x: x + 1`
  - `def f(x): return x + 1`

## 三項演算子
`(変数) = (条件がTrueのときの値) if (条件) else (条件がFalseのときの値)`

## pass
- 何もしない