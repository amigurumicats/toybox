# 概要
1ファイルで完結する小さいスクリプト置き場。  
下にいけばいくほど古い。  

## atcoder_color
AtCoderのコンテスト成績表(users/*/history)のテーブルをいい感じに着色するChrome拡張機能。


## shindanmaker_scraper.py
診断メーカーの名前をランダムにしてその結果を取得するスクレイパー。対診断メーカー謎。


## wcl_each_lang.sh
「お前は今まで書いたコードの行数を覚えているのか？」  
usage: `./wcl_each_lang.sh {dir}`  
ex. `./wcl_each_lang.sh .`  
指定したフォルダ以下の`*.py`とか`*.js`とかの総行数とかファイル数とかを数えて出力するシェルスクリプト。


## helpTransPaper
論文(の一部)などをgoogle翻訳にかけるときに便利なブックマークレット。  
改行とか単語内改行とかを消去するやつ。  


## lifegame と lifegame_new.py
python3.x+pygame1.9でライフゲーム作ったやつ。  
`lifegame.py`が2016年9月に作ったやつで、`lifegame_new.py`がそれを2018年10月にリファクタしたやつ。  
生物ありが白、なしが黒。  
`esc` : 終了  
`方向キー` : 移動(黄色い縁)  
`space` : 黄色い縁のマスの白と黒が入れ替わる  
`s` : スタート/停止  
`n` : 次の世代へ  
`r` : ランダム初期化  
`c` : 全消去  
`k` : 加速/減速  
