# sklearn
sklearnでは、clfで宣言するモデルを切り替えるだけで機械学習アルゴリズムを差し替えられます
```py
# 学習定義
## ロジスティック回帰
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(penalty='l2', solver='sag', random_state=0)

## ランダムフォレスト
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)

# 学習・予測
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
```

# LightGBM
LightGBMは大量の決定木を作成しながら学習を進めるため、過学習が発生しやすい
→学習に利用しない検証用のデータに対する性能を見ながら学習を打ち切る「early stopping」を利用する

```py
# 学習用・検証用にデータセットを分割する
from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.3, random_state=0, stratify=y_train)
# LightGBMでは、カテゴリ変数に対して特別な処理28を自動的に実行してくれる
## カテゴリ変数をリスト形式で宣言する
categorical_features = ['Embarked', 'Pclass', 'Sex']

# 学習・予測
import lightgbm as lgb
lgb_train = lgb.Dataset(X_train, y_train, categorical_feature=categorical_features)
lgb_eval = lgb.Dataset(X_valid, y_valid, reference=lgb_train, categorical_feature=categorical_features)

params = {
    'objective': 'binary'
}

model = lgb.train(params, lgb_train,
                  valid_sets=[lgb_train, lgb_eval],
                  verbose_eval=10,
                  num_boost_round=1000,
                  early_stopping_rounds=10)

y_pred = model.predict(X_test, num_iteration=model.best_iteration)
```