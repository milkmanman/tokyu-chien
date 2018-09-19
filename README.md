東急線通知スクリプト
====

python初心者がpython3.6で書いた通知用スクリプトです  
LINE notify (https://notify-bot.line.me/ja/) に登録が必要です。

## 必要モジュール  
 - BeautifulSoup  

それ以外は標準で入っているはずなのでたぶん行けます  

## 使い方  

setting.iniに必要な情報を入力(コメント参照)  
lineに関しては以下の通り  

| 路線名 | line |
----|---- 
| 東横線 | touyoko |
| 目黒線 | meguro |
| 田園都市線 | dento |
| 大井町線 | oimachi |
| 池上線 | ikegami |
| 東急多摩川線 | tamagawa |
| こどもの国線 | kodomo |
| 世田谷線 | setagaya |


```
python3.6 cl.py
```
などと単純に実行すれば当日分の下りの遅延情報がLINEにpushされます  
cronに仕込んで使うことを想定しています  

## 注意  
スクレイピングなので実行しすぎないようにしてください  

## 今後の実装  
 - ほかの路線にも対応 <-全路線対応
 - ログ機能？
 - 遅延がなかった場合の出し分け対応
