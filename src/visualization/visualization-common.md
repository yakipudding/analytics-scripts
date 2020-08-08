
## 2つのグラフを並べる（ヒストグラム）
```py
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
tweet_len=tweet[tweet['target']==1]['text'].str.len()
ax1.hist(tweet_len,color='red')
ax1.set_title('disaster tweets')
tweet_len=tweet[tweet['target']==0]['text'].str.len()
ax2.hist(tweet_len,color='green')
ax2.set_title('Not disaster tweets')
fig.suptitle('Characters in tweets')
plt.show()
```

## タプルの配列からソートしてxy軸作成
```py
# TOP10を描画
top=sorted(dic.items(), key=lambda x:x[1],reverse=True)[:10] 
#  top:[('the', 1524),('a', 1115), ...] タプルの配列
# *top:('the', 1524) ('a', 1115)... ※要素がアンパックされる
x,y=zip(*top) # zip:複数リストの要素を取得
# x:('the','a',...) y:(1524,1115,...)
plt.bar(x,y)
```